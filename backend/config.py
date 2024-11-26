import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('742017ac5bc11f63240904b796393395d908c4bb4cc8030641f43a389ddbc0d0')
    SQLALCHEMY_DATABASE_URI = os.getenv('postgresql://danjmeehan:Tra1n1ng!@localhost:5432/training_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STRAVA_CLIENT_ID = os.getenv('141014')
    STRAVA_CLIENT_SECRET = os.getenv('2b36bb82476858a3e0def6c385c32022d24eb2df')