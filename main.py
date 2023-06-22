import streamlit as st
import os
import time
from helpers import uploadToS3
from llama_index import VectorStoreIndex, SimpleDirectoryReader
import boto3
import s3fs
import pathlib

p = pathlib.Path("data/")
p.mkdir(parents=True, exist_ok=True)
st.title('chatmydocs AI')
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
s3 = s3fs.S3FileSystem(key=os.environ['AWS_ACCESS_KEY_ID'], secret=os.environ['AWS_SECRET_ACCESS_KEY'])

c1, c2 = st.columns(2)
c1.subheader('Upload word/pdf File')
uploaded_files = st.file_uploader("Choose a word/pdf file")

if uploaded_files is not None:
  st.write("Filename:", uploaded_files.name)
  uploadToS3(file=uploaded_files, bucket=os.environ['AWS_S3BUCKET'], s3_file=uploaded_files)
  obj = boto3.client("s3")
  obj.download_file(Filename="data/" + uploaded_files.name,
                    Bucket=os.environ['AWS_S3BUCKET'],
                    Key=uploaded_files.name)

  title = st.text_area('What do you curious about?')
  sbutton = st.button('Submit')
  if sbutton:
    documents = SimpleDirectoryReader('data/').load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    with st.spinner("Analyzing..."):
      time.sleep(5)

    response = query_engine.query(
      "Becoming an intelligent subject expert and humorist, Respond the following query, "
      + title)
    print(response)
    st.write(str(response))
#     st.write("Please note this feature is under development right now.")
    try:
      file_path = pathlib.Path('data/' + uploaded_files.name)
      file_path.unlink()
      st.write(str('file deleted ' + uploaded_files.name))
    except:
      st.write(str("File doesn't exist +" + uploaded_files.name))
