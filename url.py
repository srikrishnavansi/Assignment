import os
import streamlit as st
import requests
from bs4 import BeautifulSoup
import pdfplumber
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# Load API key from .env
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

st.set_page_config(page_title="Gemini 1.5 Flash Summarizer", layout="centered")
st.title("📄🔗 Gemini 1.5 Flash Summarizer")
st.write("Summarize a PDF file or a web page using Gemini 1.5 Flash and LangChain.")

# --- PDF Extraction ---
def extract_text_from_pdf(uploaded_file):
    try:
        with pdfplumber.open(uploaded_file) as pdf:
            texts = [page.extract_text() for page in pdf.pages if page.extract_text()]
            return "\n".join(texts)
    except Exception as e:
        return None

# --- Web Content Extraction ---
def fetch_web_content(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = [p.get_text() for p in soup.find_all("p")]
        content = " ".join(paragraphs)
        return content.strip()
    except Exception as e:
        return None

# --- Summarization using Gemini 1.5 Flash ---
def summarize_content(content, api_key):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0, google_api_key=api_key)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert assistant. Extract the key information and generate a concise summary of the following content in a detailed way and improve the view of the summary"),
        ("human", "{content}")
    ])
    chain = prompt | llm
    result = chain.invoke({"content": content})
    return result.content

# --- Streamlit UI ---
option = st.radio("Choose input type:", ("PDF File", "Web URL"))

content = None

if option == "PDF File":
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if uploaded_file is not None:
        with st.spinner("Extracting text from PDF..."):
            content = extract_text_from_pdf(uploaded_file)
        if not content:
            st.error("Could not extract text from the PDF. Please check the file.")
elif option == "Web URL":
    url = st.text_input("Enter the URL to summarize:", "")
    if url:
        with st.spinner("Fetching content from URL..."):
            content = fetch_web_content(url)
        if not content:
            st.error("Could not fetch or extract content from the URL.")

if content:
    if st.button("Summarize"):
        if not GOOGLE_API_KEY:
            st.error("Google Gemini API key not found. Please set it in your .env file.")
        else:
            with st.spinner("Summarizing..."):
                summary = summarize_content(content, GOOGLE_API_KEY)
            st.subheader("Summary")
            st.info(summary)
