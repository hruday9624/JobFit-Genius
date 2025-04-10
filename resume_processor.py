def evaluate_fit(resume_text, jd_text, mode="basic", llm=None):
    """
    Evaluate the fit between the resume and job description.

    Args:
        resume_text (str): The extracted resume content.
        jd_text (str): The extracted job description content.
        mode (str): Either 'basic' or 'llm'.
        llm (LLMInterface, optional): Required only if mode is 'llm'.

    Returns:
        dict: {
            "score": float,
            "summary": str,
            "matching_keywords": list,
            "suggestions": list
        }
    """

    if mode == "basic":
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity

        vectorizer = TfidfVectorizer(stop_words="english")
        vectors = vectorizer.fit_transform([resume_text, jd_text])
        score = cosine_similarity(vectors[0], vectors[1])[0][0] * 100

        # Get top keywords from JD that match resume
        jd_keywords = set(jd_text.lower().split())
        resume_keywords = set(resume_text.lower().split())
        matching = list(jd_keywords & resume_keywords)

        return {
            "score": round(score, 2),
            "summary": f"Basic fit score: {score:.2f}%",
            "matching_keywords": matching,
            "suggestions": ["Consider tailoring your resume to better reflect key job terms."]
        }

    elif mode == "llm":
        if not llm:
            raise ValueError("LLM object must be provided in 'llm' mode.")

        prompt = f"""
        Compare the following resume and job description. 
        Give a score out of 100, mention strengths, weaknesses, and suggestions.

        ### Resume:
        {resume_text}

        ### Job Description:
        {jd_text}
        """
        response = llm.invoke(prompt)

        return {
            "score": extract_score(response),
            "summary": extract_summary(response),
            "matching_keywords": extract_keywords(response),
            "suggestions": extract_suggestions(response)
        }

    else:
        raise ValueError("Mode must be either 'basic' or 'llm'")
