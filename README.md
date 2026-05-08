# Resume_Analyzer
AI Resume Analyzer using Streamlit and Groq API to compare resumes with job descriptions and provide insights.
# AI Resume Analyzer

## Overview
This project analyzes resumes against job descriptions using AI and provides insights such as match score, missing skills, and improvement suggestions.

## Features
- Upload resume (PDF)
- Enter job description
- AI-based match percentage
- Missing skills detection
- Suggestions for improvement
- Enhanced resume bullet points

## Tech Stack
- Python
- Streamlit
- Groq API (LLaMA 3)
- PyPDF2

## How It Works
1. Upload a resume (PDF)
2. Enter a job description
3. The system extracts text from the resume
4. AI compares resume and job description
5. Results are generated with insights

## Setup
1. Install dependencies:
   pip install -r requirements.txt

2. Run the app:
   streamlit run app.py

## Use Case
Helps job seekers improve resumes and optimize for ATS systems.