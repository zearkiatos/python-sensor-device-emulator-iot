import os
from dotenv import load_dotenv

environment = os.getenv('FLASK_ENV')

load_dotenv(dotenv_path='.env')

class Config:
    ENVIRONMENT = environment
    APP_NAME=os.getenv('APP_NAME')
    USER=os.getenv('USER_MQTT')
    PASSWORD=os.getenv('PASSWORD')