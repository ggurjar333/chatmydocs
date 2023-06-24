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
        self._folder_name = ""
        self._filename = ""
        self._loc_path = ""

    def upload(self, file_obj):
        self._filename = file_obj.name
        obj.upload_fileobj(file_obj, bucket, file_obj.name)

    def download(self, file_obj, temp_dir):
        self._filename = file_obj.name
        self._folder_name = temp_dir
        self._loc_path = temp_dir + '/' + file_obj.name

        temp_dir = Utility()
        temp_dir.create_tmp_folder(self._folder_name)
        obj.download_file(Filename=self._loc_path,
                          Bucket=bucket,
                          Key=file_obj.name)

    def __str__(self) -> str:
        return f'This {self._filename} was temporarily downloaded at {self._loc_path}. and then deleted successfully.'
