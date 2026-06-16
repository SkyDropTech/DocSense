import requests
from app.config import settings

def generate_summary(text: str) -> str:
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": f"Bearer {settings.HUGGINGFACE_API_KEY}"}
    
    payload = {
        "inputs": text,
        "parameters": {"max_length": 150, "min_length": 40, "do_sample": False}
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            return response.json()[0]['summary_text']
        else:
            return f"API Error ({response.status_code}): {response.text}"
            
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to the AI API. Please check your internet connection or VPN settings."
    except requests.exceptions.Timeout:
        return "Error: The AI API took too long to respond. Please try again."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"