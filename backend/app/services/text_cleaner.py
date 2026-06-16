import re

def clean_text(text: str) -> str:
    # Remove extra whitespace and newlines
    cleaned = re.sub(r'\s+', ' ', text)
    # Truncate text to avoid hitting API token limits (approx 3000 words for this example)
    words = cleaned.split()
    if len(words) > 3000:
        cleaned = " ".join(words[:3000])
    return cleaned.strip()