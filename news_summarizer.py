import requests
from bs4 import BeautifulSoup
import json
import os
from dotenv import load_dotenv

load_dotenv()

NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
TAVILY_API_KEY = os.getenv("TAVILLY_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MIN_ARTICLES = 5


# -------------------------------------------
def search_newsapi(query):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "apiKey": NEWSAPI_KEY,
        "pageSize": 20,
        "sortBy": "relevancy",
        "language": "en"
    }

    resp = requests.get(url, params=params)
    data = resp.json()

    if "articles" not in data:
        print("NewsAPI ERROR:", data)
        return []

    results = []
    for a in data["articles"]:
        results.append({
            "title": a["title"],
            "url": a["url"],
            "source": "newsapi",
            "description": a.get("description", "")
        })
    return results


# -------------------------------------------
def search_tavily(query, seen_urls):
    tavily_url = "https://api.tavily.com/search"

    payload = {
        "api_key": TAVILY_API_KEY,
        "query": query,
        "max_results": 20
    }

    resp = requests.post(tavily_url, json=payload)
    data = resp.json()

    if "results" not in data:
        print("Tavily ERROR:", data)
        return []

    results = []
    for item in data["results"]:
        if item["url"] not in seen_urls:
            results.append({
                "title": item.get("title", ""),
                "url": item["url"],
                "source": "tavily",
                "description": item.get("snippet", "")
            })
    return results


# -------------------------------------------
def scrape_text(url):
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        text = "\n".join([p.get_text() for p in soup.find_all("p")])
        return text.strip()
    except:
        return ""


# -------------------------------------------
def gather_articles(query):
    news_results = search_newsapi(query)
    seen = {a["url"] for a in news_results}

    tavily_results = search_tavily(query, seen)

    all_articles = news_results + tavily_results

    final = []
    for art in all_articles:
        text = scrape_text(art["url"])
        if len(text) > 200:
            art["text"] = text
            final.append(art)

    return final


# -------------------------------------------
def filter_relevant(query, articles, top_n=5):
    scored = []
    for art in articles:
        score = sum(art["text"].lower().count(w.lower()) for w in query.split())
        scored.append((score, art))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [a for score, a in scored[:top_n]]


# -------------------------------------------
def call_llm_for_json(question, articles):
    from langchain_openai import ChatOpenAI
    llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)

    system_prompt = """
You are a factual news summarizer.
Return ONLY valid JSON:
{
   "question": "",
   "summary": "",
   "articles_used": [
      {"title": "", "url": "", "source": ""}
   ]
}
"""

    content = {
        "question": question,
        "articles": [
            {"title": a["title"], "url": a["url"], "source": a["source"], "text": a["text"]}
            for a in articles
        ]
    }

    result = llm.invoke([
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": json.dumps(content)}
    ])

    return result.content


# -------------------------------------------
def summarize_news(question):
    articles = gather_articles(question)

    if len(articles) == 0:
        return {"error": "No articles found."}

    selected = filter_relevant(question, articles)
    json_output = call_llm_for_json(question, selected)

    return json.loads(json_output)
