# from dotenv import load_dotenv

# load_dotenv()

# import streamlit as st
# import os
# from PIL import Image
# import fitz

# import google.generativeai as genai

# # Check if the Google API key is set
# google_api_key = os.getenv("GOOGLE_API_KEY")
# if not google_api_key:
#     st.error("Google API key is not set. Please set it using environment variables.")
#     st.stop()

# genai.configure(api_key=google_api_key)

# def get_gemini_response(input_text, pdf_content, prompt):
#     model = genai.GenerativeModel('gemini-pro')
#     response = model.generate_content([input_text, pdf_content, prompt])
#     return response.text

# def input_pdf_setup(uploaded_file):
#     if uploaded_file is not None:
#         try:
#             # Read the PDF file
#             document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
#             # Initialize a list to hold the text of each page
#             text_parts = []

#             # Iterate over the pages of the PDF to extract the text
#             for page in document:
#                 text_parts.append(page.get_text())

#             # Concatenate the list into a single string with a space in between each part
#             pdf_text_content = " ".join(text_parts)
#             return pdf_text_content
#         except Exception as e:
#             st.error(f"Error reading PDF file: {e}")
#             st.stop()
#     else:
#         st.error("No file uploaded")
#         st.stop()

# ## Streamlit App

# st.set_page_config(page_title="Resume Expert")

# st.header("Resume Analyzer")
# st.subheader('Analyze your resume and get help to get selected faster')
# input_text = st.text_input("Job Description: ", key="input")
# uploaded_file = st.file_uploader("Upload your Resume(PDF)...", type=["pdf"])
# pdf_content = ""

# if uploaded_file is not None:
#     st.write("PDF Uploaded Successfully")

# submit1 = st.button("Tell Me About the Resume")
# submit2 = st.button("How Can I Improve My Skills")
# submit3 = st.button("What Are the Keywords That Are Missing")
# submit4 = st.button("Percentage Match")
# submit5 = st.button("Answer My Query")

# input_promp = st.text_input("Queries: Feel Free to Ask here")

# input_prompt1 = """
# You are an experienced Technical Human Resource Manager, your task is to review the provided resume against the job description. 
# Please share your professional evaluation on whether the candidate's profile aligns with the role. 
# Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
# """

# input_prompt2 = """
# You are an Technical Human Resource Manager with expertise in data science, 
# your role is to scrutinize the resume in light of the job description provided. 
# Share your insights on the candidate's suitability for the role from an HR perspective. 
# Additionally, offer advice on enhancing the candidate's skills and identify areas where improvement is needed.
# """

# input_prompt3 = """
# You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
# your task is to evaluate the resume against the provided job description. As a Human Resource manager,
# assess the compatibility of the resume with the role. Give me what are the keywords that are missing.
# Also, provide recommendations for enhancing the candidate's skills and identify which areas require further development.
# """

# input_prompt4 = """
# You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
# your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
# the job description. First the output should come as percentage and then keywords missing and last final thoughts.
# """

# if submit1:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_text, pdf_content, input_prompt1)
#         st.subheader("The Response is")
#         st.write(response)
#     else:
#         st.error("Please upload a PDF file to proceed.")

# elif submit2:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_text, pdf_content, input_prompt2)
#         st.subheader("The Response is")
#         st.write(response)
#     else:
#         st.error("Please upload a PDF file to proceed.")

# elif submit3:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_text, pdf_content, input_prompt3)
#         st.subheader("The Response is")
#         st.write(response)
#     else:
#         st.error("Please upload a PDF file to proceed.")

# elif submit4:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_text, pdf_content, input_prompt4)
#         st.subheader("The Response is")
#         st.write(response)
#     else:
#         st.error("Please upload a PDF file to proceed.")

# elif submit5:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_promp, pdf_content, input_text)
#         st.subheader("The Response is")
#         st.write(response)
#     else:
#         st.error("Please upload a PDF file to proceed.")
# import streamlit as st
# import os
# from PIL import Image
# import fitz
# import google.generativeai as genai

# # Set your Google Gemini API key here
# google_api_key = "GEMINI_API_KEY"  # Replace with your actual API key

# if not google_api_key:
#     st.error("Google API key is not set. Please set it in the script.")
#     st.stop()

# # Configure Gemini AI
# genai.configure(api_key=google_api_key)

# def get_gemini_response(input_text, pdf_content, prompt):
#     model = genai.GenerativeModel('gemini-2.0-flash')  # Using the specified model
#     response = model.generate_content([input_text, pdf_content, prompt])
#     return response.text

# def input_pdf_setup(uploaded_file):
#     if uploaded_file is not None:
#         try:
#             document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
#             text_parts = [page.get_text() for page in document]
#             pdf_text_content = " ".join(text_parts)
#             return pdf_text_content
#         except Exception as e:
#             st.error(f"Error reading PDF file: {e}")
#             st.stop()
#     else:
#         st.error("No file uploaded")
#         st.stop()

# ## Streamlit App
# st.set_page_config(page_title="Resume Expert")
# st.header("Resume Analyzer")
# st.subheader('Analyze your resume and get help to get selected faster')

# input_text = st.text_input("Job Description:", key="input")
# uploaded_file = st.file_uploader("Upload your Resume (PDF)...", type=["pdf"])

# if uploaded_file is not None:
#     st.write("PDF Uploaded Successfully")

# submit1 = st.button("Tell Me About the Resume")
# submit2 = st.button("How Can I Improve My Skills")
# submit3 = st.button("What Are the Keywords That Are Missing")
# submit4 = st.button("Percentage Match")
# submit5 = st.button("Answer My Query")

# input_prompt1 = """
# You are an experienced Technical Human Resource Manager. Review the resume against the job description.
# Provide an evaluation, highlighting strengths and weaknesses.
# """

# input_prompt2 = """
# You are a Technical HR Manager with expertise in data science. Evaluate the resume and suggest skill improvements.
# """

# input_prompt3 = """
# You are an ATS scanner. Identify missing keywords from the resume compared to the job description.
# """

# input_prompt4 = """
# You are an ATS scanner. Provide a percentage match between the resume and job description, followed by missing keywords and final thoughts.
# """

# input_promp = st.text_input("Queries: Feel Free to Ask here")

# if submit1 and uploaded_file:
#     pdf_content = input_pdf_setup(uploaded_file)
#     response = get_gemini_response(input_text, pdf_content, input_prompt1)
#     st.subheader("The Response is")
#     st.write(response)

# elif submit2 and uploaded_file:
#     pdf_content = input_pdf_setup(uploaded_file)
#     response = get_gemini_response(input_text, pdf_content, input_prompt2)
#     st.subheader("The Response is")
#     st.write(response)

# elif submit3 and uploaded_file:
#     pdf_content = input_pdf_setup(uploaded_file)
#     response = get_gemini_response(input_text, pdf_content, input_prompt3)
#     st.subheader("The Response is")
#     st.write(response)

# elif submit4 and uploaded_file:
#     pdf_content = input_pdf_setup(uploaded_file)
#     response = get_gemini_response(input_text, pdf_content, input_prompt4)
#     st.subheader("The Response is")
#     st.write(response)

# elif submit5 and uploaded_file:
#     pdf_content = input_pdf_setup(uploaded_file)
#     response = get_gemini_response(input_promp, pdf_content, input_text)
#     st.subheader("The Response is")
#     st.write(response)

# elif not uploaded_file:
#     st.error("Please upload a PDF file to proceed.")



import streamlit as st
import os
from PIL import Image
import fitz
import google.generativeai as genai

# Set the Google API key directly
google_api_key = "GEMINI_API_KEY"  # Replace with the actual API key

if not google_api_key:
    st.error("Google API key is not set. Please provide a valid API key.")
    st.stop()

genai.configure(api_key=google_api_key)

def get_gemini_response(input_text, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content([input_text, pdf_content, prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        try:
            document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
            text_parts = [page.get_text() for page in document]
            return " ".join(text_parts)
        except Exception as e:
            st.error(f"Error reading PDF file: {e}")
            st.stop()
    else:
        st.error("No file uploaded")
        st.stop()

# Streamlit App
st.set_page_config(page_title="Resume Expert")

st.header("Resume Analyzer")
st.subheader('Analyze your resume and get help to get selected faster')
input_text = st.text_input("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your Resume(PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1 = st.button("Tell Me About the Resume")
submit2 = st.button("How Can I Improve My Skills")
submit3 = st.button("What Are the Keywords That Are Missing")
submit4 = st.button("Percentage Match")
submit5 = st.button("Answer My Query")

input_promp = st.text_input("Queries: Feel Free to Ask here")

input_prompt1 = """You are an experienced Technical Human Resource Manager..."""
input_prompt2 = """You are a Technical Human Resource Manager with expertise in data science..."""
input_prompt3 = """You are a skilled ATS scanner with a deep understanding of data science..."""
input_prompt4 = """You are a skilled ATS scanner, give me the percentage match..."""

if submit1 and uploaded_file:
    pdf_content = input_pdf_setup(uploaded_file)
    response = get_gemini_response(input_text, pdf_content, input_prompt1)
    st.subheader("The Response is")
    st.write(response)
elif submit2 and uploaded_file:
    pdf_content = input_pdf_setup(uploaded_file)
    response = get_gemini_response(input_text, pdf_content, input_prompt2)
    st.subheader("The Response is")
    st.write(response)
elif submit3 and uploaded_file:
    pdf_content = input_pdf_setup(uploaded_file)
    response = get_gemini_response(input_text, pdf_content, input_prompt3)
    st.subheader("The Response is")
    st.write(response)
elif submit4 and uploaded_file:
    pdf_content = input_pdf_setup(uploaded_file)
    response = get_gemini_response(input_text, pdf_content, input_prompt4)
    st.subheader("The Response is")
    st.write(response)
elif submit5 and uploaded_file:
    pdf_content = input_pdf_setup(uploaded_file)
    response = get_gemini_response(input_promp, pdf_content, input_text)
    st.subheader("The Response is")
    st.write(response)
