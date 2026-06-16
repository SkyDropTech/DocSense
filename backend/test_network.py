import requests

print("Running Network Diagnostics...\n")

try:
    print("Test 1: Pinging Google (Checking general internet)...")
    requests.get("https://www.google.com", timeout=5)
    print("✅ Success: Python can reach the internet.\n")
    
    print("Test 2: Pinging Hugging Face (Checking DNS)...")
    requests.get("https://huggingface.co", timeout=5)
    print("✅ Success: Python can resolve Hugging Face.\n")
    
    print("Test 3: Pinging API Inference (Checking API domain)...")
    requests.get("https://api-inference.huggingface.co", timeout=5)
    print("✅ Success: Python can reach the API domain.\n")

except requests.exceptions.ConnectionError as e:
    print(f"\n❌ FAILED: Connection Error.\nDetails: {e}")
except requests.exceptions.Timeout:
    print("\n❌ FAILED: The connection timed out.")
except Exception as e:
    print(f"\n❌ FAILED: An unexpected error occurred: {e}")