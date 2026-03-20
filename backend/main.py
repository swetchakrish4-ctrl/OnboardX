# backend/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

# Relative imports (make sure __init__.py exists in backend/)
from .skill_extractor import extract_skills_with_levels
from .gap_analyzer import analyze_gap
from .adaptive_engine import generate_path
from .reasoning import generate_reasoning

# Initialize FastAPI
app = FastAPI(title="OnboardX - Adaptive Onboarding Engine")

# Pydantic model for request body
class InputData(BaseModel):
    resume: str
    job_description: str

# Safe path to course catalog JSON
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
COURSE_CATALOG_PATH = os.path.join(BASE_DIR, "../data/course_catalog.json")

with open(COURSE_CATALOG_PATH, "r", encoding="utf-8") as f:
    course_catalog = json.load(f)

# Map generated path to courses
def map_courses(path):
    result = []
    for skill, level in path:
        result.append({
            "skill": skill,
            "level": level,
            "courses": course_catalog.get(skill, [])
        })
    return result

# Optional root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to OnboardX 🚀 Adaptive Onboarding Engine"}

# Main endpoint for generating personalized learning path
@app.post("/generate")
def generate(data: InputData):
    try:
        # Extract skills from resume
        resume_skills = extract_skills_with_levels(data.resume)

        # Use course catalog skills as JD skills
        jd_skills = list(course_catalog.keys())

        # Analyze gaps
        gap = analyze_gap(resume_skills, jd_skills)

        # Targets to learn
        targets = gap.get("missing", []) + gap.get("weak", [])

        # Generate optimized adaptive path
        path = generate_path(targets, resume_skills)

        # Map path to actual courses
        learning_path = map_courses(path)

        # Generate reasoning trace
        reasoning = generate_reasoning(targets)

        # Calculate approximate time saved
        experienced_skills = [s for s in resume_skills if s in jd_skills]
        time_saved = f"{min(50, len(experienced_skills)*10)}% reduction in training time"

        return {
            "resume_skills": resume_skills,
            "gap": gap,
            "learning_path": learning_path,
            "reasoning": reasoning,
            "time_saved": time_saved
        }

    except Exception as e:
        # Catch errors and return as JSON for debugging
        return {"error": str(e)}