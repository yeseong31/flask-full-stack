import os.path

from dotenv import load_dotenv

# https://velog.io/@yvvyoon/python-env-dotenv
load_dotenv(verbose=True)

SECRET_KEY = os.getenv('SECRET_KEY')
