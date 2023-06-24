import boto3
import os
from dotenv import load_dotenv
from utilities import Utility
load_dotenv()

bucket = os.environ.get('AWS_S3BUCKET')
obj = boto3.client('s3',
                   aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                   aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])


class S3helpers:
    def __init__(self):
        self._temp_folder = ""
        self._filename = ""

    def upload(self, file_obj):
        self._filename = file_obj.name
        obj.upload_fileobj(file_obj, bucket, file_obj.name)

    def download(self, file_obj, temp_folder):
        self._filename = file_obj.name
        self._temp_folder = temp_folder + '/'
        file_path = self._temp_folder + self._filename

        # Create a temp directory
        ut = Utility()
        ut.create_tmp_folder(folder_name=self._temp_folder)

        obj.download_file(Filename= file_path,
                          Bucket=bucket,
                          Key=file_obj.name)

    def __str__(self) -> str:
        return str(f'{self._filename} is on s3.')
