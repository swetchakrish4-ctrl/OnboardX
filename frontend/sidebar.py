import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.title("📂 Data Input")
        st.markdown("---")
        
        uploaded_file = st.file_uploader(
            "Upload Candidate Profile", 
            type=['pdf', 'pptx', 'eml'],
            help="Supports PDF Resumes, PPT Portfolios, and EML Referrals"
        )
        
        jd_text = st.text_area(
            "Target Job Description", 
            height=250,
            placeholder="Paste the JD here..."
        )
        
        st.divider()
        run_btn = st.button("🚀 Run Intelligent Analysis", use_container_width=True)
        
        return uploaded_file, jd_text, run_btn