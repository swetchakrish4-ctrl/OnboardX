def analyze_gap(resume_skills, jd_skills):
    missing = []
    weak = []

    for skill in jd_skills:
        if skill not in resume_skills:
            missing.append(skill)
        elif resume_skills[skill] == "Beginner":
            weak.append(skill)

    return {"missing": missing, "weak": weak}