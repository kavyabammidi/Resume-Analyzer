from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PyPDF2 import PdfReader

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini API
if API_KEY is None:
    st.error("⚠️ API Key is missing! Please check your .env file.")
else:
    genai.configure(api_key=API_KEY)

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    try:
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text.strip() if text else "No text found in the PDF."
    except Exception as e:
        st.error(f"Error extracting text: {e}")
        return None

# Function to get AI response
def get_gemini_response(input_text, pdf_text, prompt):
    if pdf_text:
        model = genai.GenerativeModel('gemini-1.5-flash')  # Use latest model
        response = model.generate_content([input_text, pdf_text, prompt])
        return response.text
    else:
        return "No valid text extracted from the PDF."

# Streamlit UI Configuration
st.set_page_config(page_title='ATS Resume Expert', layout="centered")
st.header('📄 ATS Resume Analyzer')

# User Input
input_text = st.text_area('📌 Enter Job Description:', key='input')
uploaded_file = st.file_uploader("📂 Upload your Resume (PDF)", type=['pdf'])

if uploaded_file is not None:
    st.success('✅ PDF uploaded successfully!')

# Buttons
submit1 = st.button("📊 Analyze Resume")
submit2 = st.button("🔍 Get Percentage Match")

# AI Prompts
input_prompt1 = """
You are an experienced HR professional with expertise in Data Science, Full Stack Web Development, Big Data Engineering, DevOps, and Data Analysis.
Your task is to review the resume text against the job description. Highlight the strengths, weaknesses, and missing skills.
"""

input_prompt2 = """
You are an ATS (Application Tracking System) scanner. Evaluate the resume text against the job description.
Provide the **percentage match** and list **missing keywords** required for the job.
"""

# Processing Requests
if submit1:
    if uploaded_file is not None:
        pdf_text = extract_text_from_pdf(uploaded_file)
        if pdf_text:
            response = get_gemini_response(input_text, pdf_text, input_prompt1)
            st.subheader("📢 AI Analysis:")
            st.write(response)
        else:
            st.error("❌ Could not extract text from the PDF.")
    else:
        st.warning("⚠️ Please upload a resume first.")

elif submit2:
    if uploaded_file is not None:
        pdf_text = extract_text_from_pdf(uploaded_file)
        if pdf_text:
            response = get_gemini_response(input_text, pdf_text, input_prompt2)
            st.subheader("📊 Percentage Match & Missing Keywords:")
            st.write(response)
        else:
            st.error("❌ Could not extract text from the PDF.")
    else:
        st.warning("⚠️ Please upload a resume first.")

# import streamlit as st
# import os
# import io
# import base64
# from dotenv import load_dotenv
# from PIL import Image
# import pdf2image
# import google.generativeai as genai

# # ✅ Streamlit Page Configuration (Must be First)
# st.set_page_config(page_title='ATS Resume Expert', layout="centered")

# # ✅ Load environment variables
# load_dotenv()
# API_KEY = os.getenv("GOOGLE_API_KEY")

# # ✅ Check API Key
# if not API_KEY:
#     st.error("🚨 API Key is missing! Please check your .env file.")
# else:
#     genai.configure(api_key=API_KEY)

# # ✅ Function to Process PDF
# def input_pdf_setup(uploaded_file):
#     try:
#         images = pdf2image.convert_from_bytes(uploaded_file.read())
#         first_page = images[0]

#         img_byte_arr = io.BytesIO()
#         first_page.save(img_byte_arr, format='JPEG')
#         img_byte_arr = img_byte_arr.getvalue()

#         pdf_parts = [{
#             'mime_type': "image/jpeg",
#             'data': base64.b64encode(img_byte_arr).decode()
#         }]
#         return pdf_parts
#     except Exception as e:
#         st.error(f"Error processing PDF: {e}")
#         return None

# # ✅ Function to Get AI Response
# def get_gemini_response(input_text, pdf_content, prompt):
#     if uploaded_file is not None and pdf_content:
#         model = genai.GenerativeModel('gemini-1.5-flash')  # ✅ Updated to latest model
#         response = model.generate_content([input_text, pdf_content[0], prompt])
#         return response.text
#     else:
#         return "No valid file uploaded."

# # ✅ Streamlit UI Configuration
# st.header('📄 ATS Resume Expert')

# # ✅ User Input
# input_text = st.text_area('📝 Enter Job Description', key='input')
# uploaded_file = st.file_uploader("📤 Upload your resume (PDF)...", type=['pdf'])

# if uploaded_file is not None:
#     st.success('✅ PDF uploaded successfully!')

# # ✅ Buttons for Actions
# submit1 = st.button("📊 Analyze Resume")
# submit3 = st.button("🔍 Percentage Match")

# # ✅ AI Prompts
# input_prompt1 = """
# You are an experienced HR with expertise in Data Science, Full Stack Development, Big Data, DevOps, and Data Analysis.
# Review the provided resume against the job description and highlight strengths and weaknesses.
# """

# input_prompt3 = """
# You are an ATS scanner with a deep understanding of Data Science, Full Stack Development, Big Data, DevOps, and Data Analysis.
# Evaluate the resume against the job description and provide a **percentage match** along with missing keywords.
# """

# # ✅ Processing Requests
# if submit1:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         if pdf_content:
#             response = get_gemini_response(input_text, pdf_content, input_prompt1)
#             st.subheader("📌 AI Response:")
#             st.write(response)
#         else:
#             st.error("🚨 Error processing the PDF.")
#     else:
#         st.warning("⚠️ Please upload a resume first.")

# elif submit3:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         if pdf_content:
#             response = get_gemini_response(input_text, pdf_content, input_prompt3)
#             st.subheader("📊 Percentage Match & Missing Keywords:")
#             st.write(response)
#         else:
#             st.error("🚨 Error processing the PDF.")
#     else:
#         st.warning("⚠️ Please upload a resume first.")
