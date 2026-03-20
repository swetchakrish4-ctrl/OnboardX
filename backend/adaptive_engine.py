import json

with open("data/skill_graph.json") as f:
    skill_graph = json.load(f)

def generate_path(target_skills, user_skills):
    path = []
    visited = set()

    def dfs(skill):
        if skill in visited:
            return
        visited.add(skill)

        for prereq in skill_graph.get(skill, []):
            if prereq not in user_skills:
                dfs(prereq)

        if skill not in user_skills:
            path.append((skill, "Beginner"))
        elif user_skills[skill] == "Beginner":
            path.append((skill, "Intermediate"))

    for skill in target_skills:
        dfs(skill)

    return path