import pdfplumber
import spacy

def extract_text_from_pdf(pdf_path):
  text = ""
  with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
      text += page.extract_text() + "\n"
  return text.strip()

API_KEY = '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'

def analyze_resume_with_llm(resume_text:str, job_description:str)->dict:
  prompt = f"""
        You are an AI assistant that analyzes resumes for a software engineering job application. Given a resume and a job description, extract the following details:
        1. Identify all skills mentioned in the reusme.
        2. Calculate the total years of experience.
        3. Catogries the project based on the domain (e.g. AI, Webdevelopment, cloud etc).
        4. Rank the resume relevance to the job description on a scale of 0 to 100.

        Resume:
        {resume_text}

        Job Description:
        {job_description}

        Provide the output in valid JSON format with this structure:
        {{
            "rank": "<percentage>"
            "skills": ['skill1', 'skill2', .....]
            "total_experience": "<number of years>"
            "project_category": ['category1', 'category2',.....]
        }}

"""