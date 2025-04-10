---
title: Resume JD Fit Analyzer
emoji: 📄
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: "1.33.0"
app_file: app.py
pinned: false
---


# JD-Resume Fit Analyzer & Optimizer

A multi-agent LLM system that analyzes resume-JD fit and optimizes resumes for better ATS compatibility.

## Features

- Extract text from PDF/DOCX resumes and job descriptions
- Evaluate fit between resume and job description using AI
- Optimize resume content based on job requirements
- Web interface via Streamlit
- Preserve original tone while enhancing content

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-repo/jd-resume-analyzer.git
cd jd-resume-analyzer/Ai-Agents/Agent JD-Resume Matcher
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your-api-key-here
```

## Usage

### Web Interface
```bash
streamlit run app.py
```

### Command Line
```bash
python main.py
```

## Deployment

The application can be deployed to:
- Streamlit Cloud
- AWS EC2
- Google Cloud Run
- Any Python hosting service

## Configuration

Edit `.env` to configure:
- OpenAI API key
- Logging settings
- Default model parameters

## 📢 Licenseing Note:
This project is built for educational and demo purposes only. Commercial use or reselling of this system, UI, or logic without permission is not allowed.

Contact me if you’d like to collaborate or use this in your product.
