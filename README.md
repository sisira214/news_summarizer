
# News Summarizer 📰✨

A Python-based AI news summarization tool that fetches articles and generates concise summaries using modern NLP techniques. This project is designed to help users stay informed quickly by reducing lengthy news articles into easy-to-digest summaries.

---

## 🚀 Overview

**News Summarizer** is an AI-powered project built to retrieve the latest news articles on a given topic and produce short, meaningful summaries. It combines online news retrieval (e.g., via a News API) with generative language models to produce readable summaries for users. The tool is perfect for building personalized news digests or integrating into larger information-processing workflows.

> Note: Many similar projects use tools like the *News API* to retrieve articles and then summarize them using an LLM like OpenAI’s GPT-series within a UI such as Streamlit. :

---

## 🧠 Features

✔ Fetches current news articles on user-specified topics  
✔ Generates concise summaries using AI  
✔ Easy-to-run Python script  
✔ (Optional) Streamlit UI for interactive use  
✔ Designed to be extensible to other summarization models

---

## 🧰 Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python |
| Summarization Model | AI API (e.g., OpenAI) |
| Data Source | News API (or custom feed) |
| UI | (Optional) Streamlit |
| Dependencies | `requests`, `streamlit`, AI SDK |

---

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/sisira214/news_summarizer.git
cd news_summarizer
````

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API keys

Create a `.env` file and add your API keys (e.g., `NEWS_API_KEY`, `OPENAI_API_KEY`, etc.) as required by the scripts.

---

## 🚀 Usage

### Run the summarizer

To generate summaries:

```bash
python main.py
```

Or, if a Streamlit UI is provided:

```bash
streamlit run app.py
```

Enter a news topic or URL, and the app will display the summarized content.

---

## 🧠 How it Works

1. **Fetch articles:** The app retrieves recent news based on user input.
2. **Summarize:** It sends the article text to an AI model or summarization function.
3. **Output:** Users see short, readable summaries of each article.

This workflow enables quick comprehension of news without reading full articles. 
---

## 📁 Project Structure

```
news_summarizer/
├── .gitignore
├── README.md
├── main.py               # Main summarization script
├── app.py                # (Optional) Streamlit interface
├── requirements.txt      # Python dependencies
└── utils/                # Helper functions (fetching, processing)
```

---

## 🤝 Contributing

Contributions are welcome! You can help by:

* Improving summarization logic
* Adding support for multiple news sources
* Enhancing UI/UX
* Adding tests or CI configurations

---

## 📜 License

This project uses the **MIT License** — see the `LICENSE` file for details.

---


