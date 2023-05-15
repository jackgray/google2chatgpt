from openai import OpenAI
from openai.api_resources import Completion
import requests
import json

# Set up your API keys
google_api_key = 'YOUR_GOOGLE_API_KEY'
cse_id = 'YOUR_CSE_ID'
openai_api_key = 'YOUR_OPENAI_API_KEY'

# Set up OpenAI
openai = OpenAI(api_key=openai_api_key)

# Function to search Google
def google_search(search_term, api_key, cse_id, **kwargs):
    service_url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': search_term,
        'key': api_key,
        'cx': cse_id,
    }
    params.update(kwargs)
    response = requests.get(service_url, params=params)
    return response.json()

# Get search results from Google
results = google_search('board games', google_api_key, cse_id)

# Extract the information you want from the search results
info = ' '.join([item['snippet'] for item in results['items']])

# Use this information as part of the prompt to GPT-3
prompt = f"I have just read that: {info}. Now, can you tell me more about board games?"

response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=150)

print(response.choices[0].text.strip())
