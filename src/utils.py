import io
from typing import Union
import streamlit as st

def extract_text_from_pdf(file) -> str:
    """Extract text from PDF file"""
    try:
        import PyPDF2
        
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except ImportError:
        st.error("PyPDF2 is not installed. Please install it with: pip install PyPDF2")
        return ""
    except Exception as e:
        st.error(f"Error extracting text from PDF: {str(e)}")
        return ""

def extract_text_from_docx(file) -> str:
    """Extract text from DOCX file"""
    try:
        from docx import Document
        
        doc = Document(file)
        text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        return text
    except ImportError:
        st.error("python-docx is not installed. Please install it with: pip install python-docx")
        return ""
    except Exception as e:
        st.error(f"Error extracting text from DOCX: {str(e)}")
        return ""

def extract_text_from_file(file) -> str:
    """Extract text from uploaded file"""
    file_type = file.type
    
    if file_type == "application/pdf":
        return extract_text_from_pdf(file)
    elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return extract_text_from_docx(file)
    elif file_type == "text/plain":
        return file.read().decode()
    else:
        return ""

def format_analysis_result(result: dict) -> str:
    """Format analysis result for display"""
    formatted = ""
    for key, value in result.items():
        formatted += f"## {key.replace('_', ' ').title()}\n"
        if isinstance(value, list):
            for item in value:
                formatted += f"- {item}\n"
        elif isinstance(value, dict):
            for sub_key, sub_value in value.items():
                formatted += f"**{sub_key}:** {sub_value}\n"
        else:
            formatted += f"{value}\n"
        formatted += "\n"
    return formatted
