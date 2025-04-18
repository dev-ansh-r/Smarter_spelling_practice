import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables first
load_dotenv()  # Make sure you have a .env file in your project root

# Configure API key securely
def configure_api():
    api_key = os.getenv("GOOGLE_API_KEY")  # Get from environment variables
    
    if not api_key:
        raise ValueError("[ERROR] No API key found in environment variables")
    
    genai.configure(api_key=api_key)

# Get feedback from Gemini API
def get_feedback(word):
    try:
        configure_api()  # Ensure API is configured before use
        
        # Use the standard available model
        model = genai.GenerativeModel("gemini-1.5-pro")  # Changed to reliable model
        
        prompt = f"A student wrote the word '{word}'. Check if it's spelled correctly. If not, correct it and use it in a sentence."
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        return f"[ERROR] Gemini API error: {e}"