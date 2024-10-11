import os
from dotenv import load_dotenv

load_dotenv("config.env")

MONGODB_URL = os.getenv("MONGODB_URL")
