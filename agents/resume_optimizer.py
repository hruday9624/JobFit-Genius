import os
from openai import OpenAI
from dotenv import load_dotenv

class ResumeOptimizer:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
    def optimize_resume(self, resume_text, jd_text, preserve_tone=True):
        """
        Optimize resume based on job description
        
        Args:
            resume_text: Original resume text
            jd_text: Job description text
            preserve_tone: Whether to maintain original writing style
            
        Returns:
            Optimized resume text
        """
        # Create optimization prompt
        prompt = f"""
        Optimize this resume to better match the job description while {'maintaining the original tone and style' if preserve_tone else ''}.
        
        Job Description Requirements:
        {jd_text}
        
        Original Resume:
        {resume_text}
        
        Instructions:
        1. Focus on enhancing the Summary and Skills sections
        2. Add relevant missing keywords from the JD
        3. Keep all factual information accurate
        4. Return the full optimized resume
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert resume optimizer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        
        return response.choices[0].message.content