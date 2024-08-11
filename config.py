from dotenv import load_dotenv
import os

load_dotenv()

class Config:

    EXTERNAM_SERVICE_URL = os.getenv('EXTERNAM_SERVICE_URL')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///vervoe.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
