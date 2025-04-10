import os
from openai import OpenAI
from dotenv import load_dotenv
import re

def analyze_fit(resume_text, jd_text):
    """
    Analyze the fit between the resume and job description using GPT-4o.
    
    Args:
        resume_text (str): The extracted text from the resume.
        jd_text (str): The extracted text from the job description.
    
    Returns:
        dict: A dictionary containing:
            - analysis: Full analysis text
            - score: Numeric match score (0-100)
            - matches: List of key matching areas
            - missing: List of missing skills/keywords
    """
    # Set up OpenAI client
    load_dotenv()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # Create the prompt
    prompt = f"""
    Analyze the fit between this resume and job description:
    
    Resume:
    {resume_text}
    
    Job Description:
    {jd_text}
    
    Provide:
    1. A score from 0-100
    2. Key matching areas (bulleted list)
    3. Missing skills/keywords (bulleted list)
    Format your response with clear section headings.
    """
    
    # Get analysis from OpenAI
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a resume-JD matching expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1000
    )
    
    analysis = response.choices[0].message.content
    
    # Parse structured data from analysis
    score = re.search(r"Score:\s*(\d+)", analysis)
    score = int(score.group(1)) if score else None
    
    matches_section = re.search(r"Key matching areas:.*?(•.*?)(?=\n\n|\Z)", analysis, re.DOTALL)
    matches = [m.strip() for m in matches_section.group(1).split('•') if m.strip()] if matches_section else []
    
    missing_section = re.search(r"Missing skills/keywords:.*?(•.*?)(?=\n\n|\Z)", analysis, re.DOTALL)
    missing = [m.strip() for m in missing_section.group(1).split('•') if m.strip()] if missing_section else []
    
    return {
        "analysis": analysis,
        "score": score,
        "matches": matches,
        "missing": missing
    }
