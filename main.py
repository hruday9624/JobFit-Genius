from utils.file_extraction import extract_text
from fit_analyzer import analyze_fit
from agents.resume_optimizer import ResumeOptimizer

def main():
    print("Main function started.")
    # Example file paths (these should be replaced with user input or actual files)
    resume_path = 'Ai-Agents/Agent JD-Resume Matcher/data/HrudayMouly_GenAi_Resume_2025.pdf'
    jd_path = 'Ai-Agents/Agent JD-Resume Matcher/data/JD.pdf'

    print("Starting extraction of resume text...")
    resume_text = extract_text(resume_path)
    print("Extracted Resume Text:\n", resume_text)

    print("Resume text extraction completed.")
    print("Starting extraction of job description text...")
    jd_text = extract_text(jd_path)
    print("Extracted Job Description Text:\n", jd_text)

    print("Job description text extraction completed.")
    print("Starting fit evaluation...")
    fit_evaluation = analyze_fit(resume_text, jd_text)
    print("Fit Evaluation:\n", fit_evaluation)

    print("\nStarting resume optimization...")
    optimizer = ResumeOptimizer()
    optimized_resume = optimizer.optimize_resume(resume_text, jd_text, preserve_tone=True)
    print("\nOptimized Resume:\n", optimized_resume)

if __name__ == "__main__":
    main()