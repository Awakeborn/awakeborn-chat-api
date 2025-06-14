import requests

# Use OpenRouter or Ollama Cloud (permanent, free, fast)
API_ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = "YOUR_OPENROUTER_API_KEY"  # Get from https://openrouter.ai

def query_local_llm(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistralai/mixtral-8x7b-instruct", 
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1000
    }
    response = requests.post(API_ENDPOINT, json=data, headers=headers)
    return response.json()['choices'][0]['message']['content']
