import boto3
import streamlit as st
import time
import os


def uploadToS3(file, bucket, s3_file):
  s3 = boto3.client(
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])

  try:
    s3.upload_fileobj(file, os.environ['AWS_S3BUCKET'], s3_file.name)
    st.success('File Successfully Uploaded')
    return True
  except FileNotFoundError:
    time.sleep(9)
    st.error('File not found.')
    return False
