#REAL CODE
# from dotenv import load_dotenv

# load_dotenv()
# import base64
# import streamlit as st
# import os
# import io
# from PIL import Image 
# import pdf2image
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# def get_gemini_response(input,pdf_cotent,prompt):
#     model=genai.GenerativeModel('gemini-pro-vision')
#     response=model.generate_content([input,pdf_content[0],prompt])
#     return response.text

# def input_pdf_setup(uploaded_file):
#     if uploaded_file is not None:
#         ## Convert the PDF to image
#         images=pdf2image.convert_from_bytes(uploaded_file.read())

#         first_page=images[0]

#         # Convert to bytes
#         img_byte_arr = io.BytesIO()
#         first_page.save(img_byte_arr, format='JPEG')
#         img_byte_arr = img_byte_arr.getvalue()

#         pdf_parts = [
#             {
#                 "mime_type": "image/jpeg",
#                 "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
#             }
#         ]
#         return pdf_parts
#     else:
#         raise FileNotFoundError("No file uploaded")

# ## Streamlit App

# st.set_page_config(page_title="ATS Resume EXpert")
# st.header("ATS Tracking System")
# input_text=st.text_area("Job Description: ",key="input")
# uploaded_file=st.file_uploader("Upload your resume(PDF)...",type=["pdf"])


# if uploaded_file is not None:
#     st.write("PDF Uploaded Successfully")


# submit1 = st.button("Tell Me About the Resume")

# #submit2 = st.button("How Can I Improvise my Skills")

# submit3 = st.button("Percentage match")

# input_prompt1 = """
#  You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
#   Please share your professional evaluation on whether the candidate's profile aligns with the role. 
#  Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
# """

# input_prompt3 = """
# You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
# your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
# the job description. First the output should come as percentage and then keywords missing and last final thoughts.
# """

# if submit1:
#     if uploaded_file is not None:
#         pdf_content=input_pdf_setup(uploaded_file)
#         response=get_gemini_response(input_prompt1,pdf_content,input_text)
#         st.subheader("The Repsonse is")
#         st.write(response)
#     else:
#         st.write("Please uplaod the resume")

# elif submit3:
#     if uploaded_file is not None:
#         pdf_content=input_pdf_setup(uploaded_file)
#         response=get_gemini_response(input_prompt3,pdf_content,input_text)
#         st.subheader("The Repsonse is")
#         st.write(response)
#     else:
#         st.write("Please uplaod the resume")




#NEW1

# import os
# import io
# import base64
# import platform
# import streamlit as st
# import pdf2image
# import google.generativeai as genai
# from dotenv import load_dotenv
# from PIL import Image

# # Load environment variables
# load_dotenv()

# # Configure Google Gemini API
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Automatically detect OS and set Poppler path
# if platform.system() == "Windows":
#     POPPLER_PATH = r"C:\Program Files (x86)\poppler\Library\bin"
# else:
#     POPPLER_PATH = "/usr/bin"  # Correct path for Linux (Streamlit Cloud)

# def get_gemini_response(input, pdf_content, prompt):
#     model = genai.GenerativeModel('gemini-pro-vision')
#     response = model.generate_content([input, pdf_content[0], prompt])
#     return response.text

# def input_pdf_setup(uploaded_file):
#     if uploaded_file is not None:
#         try:
#             # Convert the PDF to images using Poppler
#             images = pdf2image.convert_from_bytes(uploaded_file.read(), poppler_path=POPPLER_PATH)
            
#             first_page = images[0]

#             # Convert first page to bytes
#             img_byte_arr = io.BytesIO()
#             first_page.save(img_byte_arr, format='JPEG')
#             img_byte_arr = img_byte_arr.getvalue()

#             pdf_parts = [
#                 {
#                     "mime_type": "image/jpeg",
#                     "data": base64.b64encode(img_byte_arr).decode()  # Encode to base64
#                 }
#             ]
#             return pdf_parts
#         except Exception as e:
#             st.error(f"Error processing PDF: {e}")
#             return None
#     else:
#         raise FileNotFoundError("No file uploaded")

# # Streamlit App
# st.set_page_config(page_title="ATS Resume Expert")
# st.header("ATS Tracking System")

# # User input for job description
# input_text = st.text_area("Job Description:", key="input")

# # Upload resume
# uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

# if uploaded_file is not None:
#     st.write("PDF Uploaded Successfully")

# # Buttons for different functionalities
# submit1 = st.button("Tell Me About the Resume")
# submit3 = st.button("Percentage match")

# # Prompts for Gemini AI
# input_prompt1 = """
# You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description. 
# Please share your professional evaluation on whether the candidate's profile aligns with the role. 
# Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
# """

# input_prompt3 = """
# You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
# Your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches 
# the job description. First, the output should come as a percentage, followed by missing keywords, and finally, overall thoughts.
# """

# # Processing based on button clicks
# if submit1:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         if pdf_content:
#             response = get_gemini_response(input_prompt1, pdf_content, input_text)
#             st.subheader("The Response is:")
#             st.write(response)
#     else:
#         st.write("Please upload the resume")

# elif submit3:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         if pdf_content:
#             response = get_gemini_response(input_prompt3, pdf_content, input_text)
#             st.subheader("The Response is:")
#             st.write(response)
#     else:
#         st.write("Please upload the resume")

# NEW 2----------------------------------------------------------------------------------------
# from dotenv import load_dotenv
# import base64
# import streamlit as st
# import os
# import io
# import time
# import platform
# from PIL import Image
# import pdf2image
# import google.generativeai as genai

# # Load environment variables
# load_dotenv()

# # Configure Google Gemini API
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Automatically detect OS and set Poppler path
# if platform.system() == "Windows":
#     POPPLER_PATH = r"C:\Program Files (x86)\poppler\Library\bin"
# else:
#     POPPLER_PATH = "/usr/bin"  # Path for Linux (Streamlit Cloud)

# def get_gemini_response(input_text, pdf_content, prompt):
#     try:
#         model = genai.GenerativeModel('gemini-pro-vision')

#         st.write("⏳ Sending request to Gemini API...")
#         start_time = time.time()

#         response = model.generate_content(
#             [input_text, pdf_content[0], prompt], 
#             request_options={"timeout": 30}  # Set a 30s timeout
#         )

#         end_time = time.time()
#         st.write(f"✅ Response received in {end_time - start_time:.2f} seconds")

#         return response.text
#     except Exception as e:
#         st.error(f"⚠️ Gemini API Timeout/Error: {e}")
#         return None

# def input_pdf_setup(uploaded_file):
#     if uploaded_file is not None:
#         try:
#             images = pdf2image.convert_from_bytes(uploaded_file.read(), poppler_path=POPPLER_PATH)

#             first_page = images[0]

#             # 🔹 Reduce image size to avoid API issues
#             first_page = first_page.resize((600, 800))  # Resize to 600x800 pixels

#             img_byte_arr = io.BytesIO()
#             first_page.save(img_byte_arr, format='JPEG', quality=50)  # Reduce quality
#             img_byte_arr = img_byte_arr.getvalue()

#             pdf_parts = [
#                 {
#                     "mime_type": "image/jpeg",
#                     "data": base64.b64encode(img_byte_arr).decode()
#                 }
#             ]
#             return pdf_parts
#         except Exception as e:
#             st.error(f"⚠️ Error processing PDF: {e}")
#             return None
#     else:
#         raise FileNotFoundError("No file uploaded")

# # Streamlit App
# st.set_page_config(page_title="ATS Resume Expert")
# st.header("ATS Tracking System")

# # User input for job description
# input_text = st.text_area("Job Description:", key="input")

# # Limit job description length to avoid API overload
# input_text = input_text[:1000]  # Limit to 1000 characters

# # Upload resume
# uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

# if uploaded_file is not None:
#     st.write("📄 PDF Uploaded Successfully")

# # Buttons for different functionalities
# submit1 = st.button("Tell Me About the Resume")
# submit3 = st.button("Percentage Match")

# # Prompts for Gemini AI
# input_prompt1 = """
# You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description. 
# Please share your professional evaluation on whether the candidate's profile aligns with the role. 
# Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
# """

# input_prompt3 = """
# You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
# Your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches 
# the job description. First, the output should come as a percentage, followed by missing keywords, and finally, overall thoughts.
# """

# # Processing based on button clicks
# if submit1:
#     if uploaded_file is not None:
#         with st.spinner("⏳ Processing resume, please wait..."):
#             pdf_content = input_pdf_setup(uploaded_file)
#             if pdf_content:
#                 response = get_gemini_response(input_prompt1, pdf_content, input_text)
#                 if response:
#                     st.subheader("📌 The Response is:")
#                     st.write(response)
#     else:
#         st.write("⚠️ Please upload the resume")

# elif submit3:
#     if uploaded_file is not None:
#         with st.spinner("⏳ Processing resume, please wait..."):
#             pdf_content = input_pdf_setup(uploaded_file)
#             if pdf_content:
#                 response = get_gemini_response(input_prompt3, pdf_content, input_text)
#                 if response:
#                     st.subheader("📌 The Response is:")
#                     st.write(response)
#     else:
#         st.write("⚠️ Please upload the resume")


#NEW 3---------------------------------------------------------------------------
from dotenv import load_dotenv
import base64
import streamlit as st
import os
import io
import time
import platform
from PIL import Image
import pdf2image
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Automatically detect OS and set Poppler path
if platform.system() == "Windows":
    POPPLER_PATH = r"C:\Program Files (x86)\poppler\Library\bin"
else:
    POPPLER_PATH = "/usr/bin"  # Path for Linux (Streamlit Cloud)

# Function to send request to Google Gemini API
def get_gemini_response(input_text, pdf_content, prompt):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')

        st.write("⏳ Sending request to Google Gemini API...")
        start_time = time.time()

        response = model.generate_content(
            [input_text, pdf_content[0], prompt], 
            request_options={"timeout": 30}  # Set a 30s timeout
        )

        end_time = time.time()
        st.write(f"✅ Response received in {end_time - start_time:.2f} seconds")

        return response.text
    except Exception as e:
        st.error(f"⚠️ Gemini API Timeout/Error: {e}")
        return None

# Function to process PDF and extract first page as an image
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        try:
            st.write("📄 Converting PDF to image...")
            images = pdf2image.convert_from_bytes(uploaded_file.read(), poppler_path=POPPLER_PATH)
            st.write("✅ PDF converted to image!")

            first_page = images[0]

            img_byte_arr = io.BytesIO()
            first_page.save(img_byte_arr, format='JPEG', quality=100)  # Keep quality high
            img_byte_arr = img_byte_arr.getvalue()

            pdf_parts = [
                {
                    "mime_type": "image/jpeg",
                    "data": base64.b64encode(img_byte_arr).decode()
                }
            ]
            st.write("✅ Image processing completed!")
            return pdf_parts
        except Exception as e:
            st.error(f"⚠️ Error processing PDF: {e}")
            return None
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit App
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")

# User input for job description
input_text = st.text_area("Job Description:", key="input")

# Upload resume (Max size: 100MB)
uploaded_file = st.file_uploader("Upload your resume (PDF, Max 100MB)...", type=["pdf"])

if uploaded_file is not None:
    if uploaded_file.size > 100 * 1024 * 1024:  # 100MB Limit
        st.error("⚠️ File too large! Please upload a resume smaller than 100MB.")
    else:
        st.write("📄 PDF Uploaded Successfully")

# Buttons for different functionalities
submit1 = st.button("Tell Me About the Resume")
submit3 = st.button("Percentage Match")

# Prompts for Gemini AI
input_prompt1 = """
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
Your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches 
the job description. First, the output should come as a percentage, followed by missing keywords, and finally, overall thoughts.
"""

# Processing based on button clicks
if submit1:
    if uploaded_file is not None:
        with st.spinner("⏳ Processing resume, please wait..."):
            pdf_content = input_pdf_setup(uploaded_file)
            if pdf_content:
                response = get_gemini_response(input_prompt1, pdf_content, input_text)
                if response:
                    st.subheader("📌 The Response is:")
                    st.write(response)
    else:
        st.write("⚠️ Please upload the resume")

elif submit3:
    if uploaded_file is not None:
        with st.spinner("⏳ Processing resume, please wait..."):
            pdf_content = input_pdf_setup(uploaded_file)
            if pdf_content:
                response = get_gemini_response(input_prompt3, pdf_content, input_text)
                if response:
                    st.subheader("📌 The Response is:")
                    st.write(response)
    else:
        st.write("⚠️ Please upload the resume")
