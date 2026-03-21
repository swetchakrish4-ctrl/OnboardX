import numpy as np
import streamlit as st
from sentence_transformers import util, SentenceTransformer

@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

def calculate_fit(res_data, jd_data):
    res_skills = [item['skill'] for item in res_data]
    jd_skills = [item['skill'] for item in jd_data]

    if not res_skills or not jd_skills:
        return 0, jd_skills

    res_vec = model.encode(" ".join(res_skills))
    jd_vec = model.encode(" ".join(jd_skills))

    fit_score = float(util.cos_sim(res_vec, jd_vec)) * 100

    res_skill_vectors = model.encode(res_skills)
    jd_skill_vectors = model.encode(jd_skills)

    similarities = util.cos_sim(jd_skill_vectors, res_skill_vectors)

    gaps = []
    for i, target in enumerate(jd_skills):
        max_sim = np.max(similarities[i].numpy())
        if max_sim < 0.65:
            gaps.append(target)

    return round(fit_score, 2), gaps