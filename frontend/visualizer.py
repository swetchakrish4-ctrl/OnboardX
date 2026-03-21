import streamlit as st
import urllib.parse


COURSE_DB = {
    "python": ("Python for Everybody (Coursera)", "https://www.coursera.org/specializations/python"),
    "machine learning": ("Machine Learning Specialization (Coursera)", "https://www.coursera.org/specializations/machine-learning-introduction"),
    "sql": ("The Complete SQL Bootcamp (Udemy)", "https://www.udemy.com/course/the-complete-sql-bootcamp/"),
    "aws": ("AWS Cloud Practitioner Essentials", "https://aws.amazon.com/training/course-descriptions/cloud-practitioner-essentials/"),
    "react": ("React - The Complete Guide (Udemy)", "https://www.udemy.com/course/react-the-complete-guide-incl-redux/"),
    "system design": ("Grokking the System Design Interview", "https://www.educative.io/courses/grokking-the-system-design-interview"),
    "docker": ("Docker Mastery (Udemy)", "https://www.udemy.com/course/docker-mastery/"),
    "kubernetes": ("Kubernetes for the Absolute Beginner", "https://www.udemy.com/course/learn-kubernetes/"),
    "cloud": ("Google Cloud Fundamentals", "https://www.coursera.org/learn/gcp-fundamentals")
}

def render_roadmap(gaps):
    if not gaps:
        st.success("🎉 Candidate is a perfect match! Focus on advanced leadership and architecture.")
        return

    st.markdown("### 📚 Personalized Learning Pathway")
    st.markdown("Based on the skill gaps identified by the AI, here are direct links to upskill:")
    
    for gap in gaps:
        gap_lower = gap.lower()
        matched_course = None
        
        
        for key, data in COURSE_DB.items():
            if key in gap_lower:
                matched_course = data
                break
        
        
        if matched_course:
            title, link = matched_course
        else:
            query = urllib.parse.quote(f"Learn {gap} full course")
            title = f"Top video tutorials for {gap}"
            link = f"https://www.youtube.com/results?search_query={query}"

        
        with st.expander(f"🔹 Gap Detected: {gap.title()}"):
            st.markdown(f"**Recommended Resource:** [{title}]({link})")
            st.markdown(f"🔗 `{link}`")