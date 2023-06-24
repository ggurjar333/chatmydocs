from dotenv import load_dotenv
import streamlit as st
import os
from helpers.s3helpers import S3helpers
import boto3
import openai
from sources.website import Website
from sources.pdfword import PdfWord
from cloud_providers.aws import AWS

load_dotenv()
title = st.title('Resume AI')
c1, c2 = st.columns(2)

# Set up cloud and openai key using UI
# c1, c2, c3 = st.columns(3)
# with c3:
#     open_ai_key = st.text_input("OpenAI API Key")
#     cloud_box = st.selectbox('Select cloud service provider', ('AWS', 'GCP', 'Azure'))
#     if cloud_box == 'AWS':
#         access_key = st.text_input('AWS Access Key ID')
#         secret_key = st.text_input('AWS Secret Access Key')
#         sbutton = st.button('Save')
#         if sbutton:
#             openai.api_key = open_ai_key
#             cloud = AWS()
#             obj = cloud.setup(access_key=access_key, secret_key=secret_key)

with c1:
    option = st.selectbox('Select Data Source', ('PDF/Word', 'Website', 'GitHub'))

    if option == 'PDF/Word':
        uploaded_files = st.file_uploader("Choose a PDF/Word file")
        if uploaded_files is not None:
            # Uploading the input file to S3 Bucket
            storage = S3helpers()
            storage.upload(file_obj=uploaded_files)
            # st.write('File Uploaded to S3.')
            storage.download(file_obj=uploaded_files, temp_folder='tmp')
            # PDF/Word Prompt Box
            query = st.text_area('Enter your prompt query')
            # st.write(query)
            # Parsing and analyzing PDF/Word
            analyze_profile = st.button('Analyze')

            if analyze_profile:
                with st.spinner('Analyzing ...'):
                    pw = PdfWord()
                    result = pw.analyze(temp_dir='tmp', user_prompt_text=query)
                if result:
                    with c2:
                        st.write(result)
                else:
                    st.write('Something went wrong')

    if option == "Website":
        url_link = st.text_input('URL')
        query = st.text_area('Enter your prompt query')
        analyze_profile = st.button('Analyze')
        if analyze_profile:
            with st.spinner('Analyzing...'):
                li = Website()
                result = li.analyze(user_website_link=url_link, user_prompt_text=query)
