from dotenv import load_dotenv
import streamlit as st
import os
import time
from s3helpers import S3helpers
from llama_index import VectorStoreIndex, SimpleDirectoryReader, download_loader
import boto3
import pathlib
import openai
from website import Website
from pdfword import PdfWord

load_dotenv()

openai.api_key = os.environ.get('OPENAI_API_KEY')
obj = boto3.client('s3',
                   aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                   aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
                   )

# p = pathlib.Path("tmp/")
# p.mkdir(parents=True, exist_ok=True)

st.title('Resume AI')

c1, c2 = st.columns(2)
# c1.subheader('Upload word/pdf File')
with c1:
    option = st.selectbox('Select Data Source', ('PDF/Word', 'LinkedIn', 'GitHub'))

    if option == 'PDF/Word':
        uploaded_files = st.file_uploader("Choose a PDF/Word file")
        if uploaded_files is not None:
            # Uploading the input file to S3 Bucket
            # try:
            storage = S3helpers()
            storage.upload(file_obj=uploaded_files)
            # st.write('File Uploaded to S3.')
            # Downloading the file from S3 to temporary system storage
            storage.download(file_obj=uploaded_files, temp_dir='tmp')
            # PDF/Word Prompt Box
            query = st.text_area('Enter your prompt query')
            st.write(query)
            # Parsing and analyzing PDF/Word
            analyze_profile = st.button('Analyze')

            if analyze_profile:
                with st.spinner('Analyzing ...'):
                    pw = PdfWord()
                    result = pw.analyze(user_prompt_text=query, temp_dir='tmp')
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
