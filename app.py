import streamlit as st
import os
from dotenv import load_dotenv
from src.resume_analyzer import ResumeAnalyzer
from src.utils import extract_text_from_pdf, extract_text_from_docx

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #1f77b4;
        margin-bottom: 30px;
    }
    .section-header {
        color: #ff7f0e;
        border-bottom: 2px solid #ff7f0e;
        padding-bottom: 10px;
        margin-top: 20px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='main-title'>🤖 AI Resume Analyzer</h1>", unsafe_allow_html=True)

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    api_provider = st.selectbox(
        "Select LLM Provider",
        ["OpenAI", "Hugging Face", "Anthropic"]
    )
    
    model_choice = st.selectbox(
        "Select Model",
        {
            "OpenAI": ["gpt-4", "gpt-3.5-turbo"],
            "Hugging Face": ["mistral-7b", "llama-2-7b"],
            "Anthropic": ["claude-3-opus", "claude-3-sonnet"]
        }.get(api_provider, [])
    )
    
    temperature = st.slider(
        "Temperature (Creativity)",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1
    )
    
    st.markdown("---")
    
    with st.expander("ℹ️ About"):
        st.info(
            """
            **AI Resume Analyzer** uses advanced LLMs to:
            - Extract and analyze resume content
            - Identify key skills and experience
            - Provide improvement suggestions
            - Generate match scores for job descriptions
            - Offer personalized recommendations
            """
        )

# Main content area
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("<h3 class='section-header'>📤 Upload Resume</h3>", unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Choose a resume file",
        type=["pdf", "docx", "txt"],
        help="Supported formats: PDF, DOCX, TXT"
    )
    
    if uploaded_file:
        st.success(f"✅ File uploaded: {uploaded_file.name}")
        
        # Extract text from uploaded file
        if uploaded_file.type == "application/pdf":
            resume_text = extract_text_from_pdf(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            resume_text = extract_text_from_docx(uploaded_file)
        else:
            resume_text = uploaded_file.read().decode()
        
        # Initialize analyzer
        analyzer = ResumeAnalyzer(
            api_provider=api_provider,
            model=model_choice,
            temperature=temperature
        )
        
        # Analysis options
        st.markdown("<h3 class='section-header'>🔍 Analysis Options</h3>", unsafe_allow_html=True)
        
        analysis_type = st.radio(
            "Select analysis type:",
            ["Complete Analysis", "Skill Extraction", "Improvement Suggestions", "Job Match Analysis"]
        )
        
        if analysis_type == "Job Match Analysis":
            job_description = st.text_area(
                "Paste job description:",
                height=200,
                placeholder="Enter the job description here..."
            )
        else:
            job_description = None
        
        if st.button("🚀 Analyze Resume", use_container_width=True):
            with st.spinner("Analyzing resume..."):
                try:
                    if analysis_type == "Complete Analysis":
                        result = analyzer.complete_analysis(resume_text)
                    elif analysis_type == "Skill Extraction":
                        result = analyzer.extract_skills(resume_text)
                    elif analysis_type == "Improvement Suggestions":
                        result = analyzer.get_improvements(resume_text)
                    elif analysis_type == "Job Match Analysis":
                        result = analyzer.match_job_description(resume_text, job_description)
                    
                    st.session_state.analysis_result = result
                except Exception as e:
                    st.error(f"❌ Error during analysis: {str(e)}")

with col2:
    st.markdown("<h3 class='section-header'>📊 Analysis Results</h3>", unsafe_allow_html=True)
    
    if "analysis_result" in st.session_state:
        result = st.session_state.analysis_result
        
        # Display results based on analysis type
        if isinstance(result, dict):
            # Display structured results
            for key, value in result.items():
                if isinstance(value, list):
                    st.subheader(key.replace('_', ' ').title())
                    for item in value:
                        st.write(f"• {item}")
                elif isinstance(value, dict):
                    st.subheader(key.replace('_', ' ').title())
                    for sub_key, sub_value in value.items():
                        st.write(f"**{sub_key}:** {sub_value}")
                else:
                    st.write(f"**{key.replace('_', ' ').title()}:** {value}")
        else:
            # Display text results
            st.markdown(result)
        
        # Download results
        st.markdown("---")
        st.download_button(
            label="📥 Download Results (JSON)",
            data=str(result),
            file_name="resume_analysis.txt",
            mime="text/plain",
            use_container_width=True
        )
    else:
        st.info("📌 Upload a resume and select analysis options to get started!")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; font-size: 0.85em;'>
    Made with ❤️ using Streamlit and AI | 
    <a href='https://github.com' target='_blank'>GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)
