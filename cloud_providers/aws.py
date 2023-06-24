import boto3


class AWS:
    def __init__(self):
        self._access_key = ""
        self._secret_key = ""

    def setup(self, access_key, secret_key):
        obj = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
        return obj


    def __str__(self):
        return f'Your AWS credentials are {self._access_key}, {self._secret_key}'