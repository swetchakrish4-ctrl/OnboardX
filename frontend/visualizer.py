import streamlit as st

def render_roadmap(gaps):
    st.header("🚀 Learning Pathway")
    for i, gap in enumerate(gaps):
        with st.container():
            st.markdown(f"**Phase {i+1}: {gap.upper()}**")
            st.caption("Target: Competency within 14 days")
            st.progress((i+1)/len(gaps))