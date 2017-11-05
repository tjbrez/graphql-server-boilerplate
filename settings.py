import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), verbose=True)

SECRET_KEY = os.environ.get("SECRET_KEY")
DATABASE_URL = os.environ.get("DATABASE_URL")
