import streamlit as st
import pandas as pd
from backend.parser import extract_text
from backend.ai_engine import get_structured_data
from backend.analytics import calculate_fit
from frontend.visualizer import render_roadmap
from frontend.sidebar import render_sidebar  


st.set_page_config(
    page_title="OnboardAI",
    page_icon="🎯",
    layout="wide"
)


if 'processed' not in st.session_state:
    st.session_state.processed = False
    st.session_state.score = 0
    st.session_state.gaps = []
    st.session_state.raw_text = ""
    st.session_state.skills = []


uploaded_file, jd_text, run_btn = render_sidebar()


if run_btn:
    if uploaded_file and jd_text:
        with st.spinner("🧠 DeepSeek-R1 is analyzing skill manifolds..."):
            try:
                
                raw_text = extract_text(uploaded_file)
                skills = get_structured_data(raw_text, "Resume")
                target = get_structured_data(jd_text, "Job Description")
                
                
                score, gaps = calculate_fit(skills, target)
                
            
                st.session_state.score = score
                st.session_state.gaps = gaps
                st.session_state.raw_text = raw_text
                st.session_state.skills = skills
                st.session_state.processed = True
                
                st.toast("Analysis Complete!", icon="✅")
            except Exception as e:
                st.error(f"Processing Error: {str(e)}")
    else:
        st.warning("⚠️ Please upload a document and paste the Job Description first.")


if st.session_state.processed:
    
    st.header("🎯 Evaluation Results")
    col1, col2, col3 = st.columns(3)
    col1.metric("Overall Fit Score", f"{st.session_state.score}%")
    col2.metric("Extracted Skills", len(st.session_state.skills))
    col3.metric("Identified Gaps", len(st.session_state.gaps))

    st.divider()

    
    col_left, col_right = st.columns(2)
    
    with col_left:
        with st.expander("📄 View Extracted Resume Text", expanded=False):
            st.text_area("Raw Content", st.session_state.raw_text, height=200)
            
    with col_right:
        with st.expander("🔍 Identified Skill Entities", expanded=True):
            if st.session_state.skills:
                
                df = pd.DataFrame(st.session_state.skills)
                st.dataframe(df, use_container_width=True)

    st.divider()

    
    st.subheader("🏁 Personalized Training Roadmap")
    if not st.session_state.gaps:
        st.success("Candidate matches all requirements! No training path needed.")
    else:
        render_roadmap(st.session_state.gaps)

else:
    
    st.image("https://img.icons8.com/illustrations/external-tulpahn-outline-color-tulpahn/400/external-online-learning-distance-learning-tulpahn-outline-color-tulpahn.png")
    st.title("Welcome to SentientPath AI")
    st.markdown("""
    ### How it works:
    1. **Upload** a Resume (PDF/PPT/Email).
    2. **Paste** the target Job Description.
    3. **AI** extracts skills and calculates semantic gaps.
    4. **Generate** a week-by-week training pathway.
    """)