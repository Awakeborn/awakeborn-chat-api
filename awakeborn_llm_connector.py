import requests

API_KEY = "your_openai_api_key"  # replace with your actual OpenAI API key
url = "https://api.openai.com/v1/chat/completions"

def query_local_llm(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    data = {
        "model": "gpt-3.5-turbo",  # or "gpt-4" if you prefer
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()

    reply = response.json()
    return reply['choices'][0]['message']['content']
