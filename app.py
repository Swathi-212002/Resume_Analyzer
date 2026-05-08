import streamlit as st
from PyPDF2 import PdfReader
from groq import Groq

import os

api_key = st.secrets["GROQ_API_KEY"]

if not api_key:
    st.error("API key not found. Please check Streamlit Secrets.")
    st.stop()

client = Groq(api_key=api_key)

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
job_desc = st.text_area("Paste Job Description")

def extract_text(pdf):
    reader = PdfReader(pdf)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

if st.button("Analyze"):
    if uploaded_file and job_desc:
        resume_text = extract_text(uploaded_file)

        prompt = f"""
        You are an AI Resume Analyzer.

        Compare the resume and job description.

        Resume:
        {resume_text}

        Job Description:
        {job_desc}

        Give:
        1. Match percentage
        2. Missing skills
        3. Suggestions
        4. Improved bullet points
        """

        response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[{"role": "user", "content": prompt}]
                    )

        result = response.choices[0].message.content
        st.subheader("Analysis Result")
        st.write(result)
    else:
        st.warning("Please upload resume and enter job description")