# backend/skill_extractor.py
import json
import os

# Load ONET skills
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ONET_PATH = os.path.join(BASE_DIR, "../data/onet_skills.json")

with open(ONET_PATH, "r", encoding="utf-8") as f:
    ONET_SKILLS = json.load(f)

def extract_skills_with_levels(text: str):
    """
    Simple local skill extractor.
    Checks which ONET skills are in the text and assigns a level.
    Returns a dict {skill: level}.
    """
    skills_found = {}
    for skill in ONET_SKILLS:
        if skill.lower() in text.lower():
            # Assign a level based on keywords in text (mock logic)
            if "expert" in text.lower() or "advanced" in text.lower():
                skills_found[skill] = "Advanced"
            elif "basic" in text.lower():
                skills_found[skill] = "Beginner"
            else:
                skills_found[skill] = "Intermediate"
    return skills_found