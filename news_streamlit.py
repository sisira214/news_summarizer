import streamlit as st
import requests

st.title("📰 AI News Summarizer")
st.write("Streamlit app loaded successfully!")

backend_url = "http://localhost:8000/summarize"

question = st.text_input("Ask about any news topic:")

if st.button("Summarize"):
    st.write("Button clicked")
    st.write("Question:", question)

    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Summarizing..."):
            try:
                resp = requests.post(backend_url, json={"question": question})
                st.write("Raw backend response:", resp.text)
                data = resp.json()

                if "error" in data:
                    st.error(data["error"])
                else:
                    st.subheader("Summary")
                    st.write(data["summary"])

                    st.subheader("Articles Used")
                    for art in data["articles_used"]:
                        st.write(f"• **{art['title']}** — [{art['url']}]({art['url']}) ({art['source']})")

            except Exception as e:
                st.error(f"Request failed: {e}")
