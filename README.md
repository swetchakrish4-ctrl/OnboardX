# OnboardAI: Next-Gen Talent Matcher



SentientPath AI is a high-performance, cross-domain talent acquisition engine powered by **DeepSeek-R1**. Unlike traditional ATS systems that rely on rigid keyword matching, SentientPath utilizes Semantic Analysis and **Explainable AI (XAI)** to bridge the gap between job requirements and candidate potential.

---

## ✨ Key Features
* **Batch Analysis:** Process multiple resumes simultaneously and generate a ranked leaderboard.
* **Explainable AI (Reasoning Trace):** We expose the internal `<think>` process of DeepSeek-R1, showing recruiters *why* the AI believes a candidate matches or lacks a skill.
* **Cross-Domain Intelligence:** Zero-shot capability across Tech, Healthcare, Legal, and Finance without manual configuration.
* **Personalized Learning Pathway:** Maps skill gaps to real-world educational resources (Coursera, Udemy, etc.).



## 🧠 Skill-Gap Analysis Logic (High-Level)

The core engine operates on a **Semantic Triple-Check** pipeline:

1.  **Entity Extraction:** Using DeepSeek-R1, the system extracts a structured JSON manifold of skills from both the Job Description (JD) and the Resume.
2.  **Normalization & Vector Mapping:** Skills are normalized (e.g., "MERN Stack" is decomposed into React, Node, etc.). We use lowercase stripping and semantic grouping to ensure "Python Developer" matches "Python Programming."
3.  **Difference Set Logic (Gap Analysis):** * Let $S_{jd}$ be the set of skills required by the employer.
    * Let $S_{res}$ be the set of skills identified in the resume.
    * The **Skill Gap** is defined as $G = S_{jd} - S_{res}$.
4.  **Reasoning Trace (XAI):** The model generates a natural language justification for the match, explaining how transferable skills (e.g., "Azure" vs "AWS") influence the final score.


## 🛠️ Tech Stack & Dependencies

* **Frontend:** Streamlit (Python)
* **Brain:** DeepSeek-R1 (1.5B) via Ollama
* **Data Parsing:** PyPDF2
* **Data Handling:** Pandas & JSON

### Dependencies
Install the required libraries using:
```bash
pip install streamlit pandas ollama PyPDF2
