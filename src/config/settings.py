# API Configuration
import os
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")
API_KEY = os.getenv("API_KEY", "your-api-key")

print(API_BASE_URL)
print(API_KEY)



# Agent Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TEMPERATURE = 0.7
MAX_ITERATIONS = 5