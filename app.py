import streamlit as st
from utils.file_extraction import extract_text
from fit_analyzer import analyze_fit
from agents.resume_optimizer import ResumeOptimizer
import logging
import traceback

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO)

def main():
    st.set_page_config(page_title="JD-Resume Fit Analyzer", layout="wide")
    st.title("📝 JD-Resume Fit Analyzer & Optimizer")
    
    with st.sidebar:
        st.header("Settings")
        preserve_tone = st.checkbox("Preserve Original Tone", value=True)
        openai_key = st.text_input("OpenAI API Key", type="password", 
                                 help="Your key is used only for this session and is not stored anywhere")
        st.caption("🔒 Privacy Note: Your OpenAI API key is used only to process your request and is never stored or logged.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Upload Resume")
        #resume_file = st.file_uploader("Choose PDF/DOCX", type=["pdf", "docx"], key="resume")
        resume_option = st.radio("Select input method:",
                                 ("Upload File", "Paste Text"),
                                 horizontal=True)

        if resume_option == "Upload File":
            resume_file = st.file_uploader("Choose PDF/DOCX", type=["pdf","docx"], key="jd")
            resume_text = ""
        else:
            resume_text = st.text_area("Paste your resume", height=200)
            resume_file = None
    
    with col2:
        st.header("Job Description")
        jd_option = st.radio("Select input method:", 
                           ("Upload File", "Paste Text"), 
                           horizontal=True)
        
        if jd_option == "Upload File":
            jd_file = st.file_uploader("Choose PDF/DOCX", type=["pdf", "docx"], key="jd")
            jd_text = ""
        else:
            jd_text = st.text_area("Paste Job Description", height=200)
            jd_file = None
    
    if st.button("Analyze & Optimize"):
        if not (resume_file or resume_text):
            st.warning("Please provide your resume")
            return
            
        if not (jd_file or jd_text):
            st.warning("Please provide job description")
            return
            
        try:
            with st.spinner("Processing..."):
                # Set API key if provided
                if openai_key:
                    import os
                    os.environ["OPENAI_API_KEY"] = openai_key
                
                # Extract resume text
                resume_text = extract_text(resume_file)
                
                # Get JD text
                if jd_file:
                    jd_text = extract_text(jd_file)
                
                # Analyze fit
                fit_evaluation = analyze_fit(resume_text, jd_text)
                
                # Optimize resume
                optimizer = ResumeOptimizer()
                optimized_resume = optimizer.optimize_resume(
                    resume_text, 
                    jd_text,
                    preserve_tone=preserve_tone
                )
                
            # Display results
            st.subheader("Fit Analysis")
            st.markdown(fit_evaluation["analysis"])
            
            st.subheader("Optimized Resume")
            st.markdown(optimized_resume)
            
            st.download_button(
                label="Download Optimized Resume",
                data=optimized_resume,
                file_name="optimized_resume.md",
                mime="text/markdown"
            )
            
        except Exception as e:
            logging.error(f"Error: {str(e)}\n{traceback.format_exc()}")
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
