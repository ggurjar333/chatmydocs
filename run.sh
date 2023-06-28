#!/bin/sh
##sudo apt-get install python3-venv
##python3 -m venv .venv
pip install wheel streamlit llama-index boto3 docx2txt streamlit-chat
streamlit run setup.py
