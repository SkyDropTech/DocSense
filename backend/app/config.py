import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
    UPLOAD_DIR = "uploads"
    
settings = Settings()

# Ensure upload directory exists
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)