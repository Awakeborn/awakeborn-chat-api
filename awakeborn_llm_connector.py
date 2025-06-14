import requests

def query_local_llm(prompt, model='mistral', stream=False):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": model,
        "prompt": prompt,
        "stream": stream
    }

    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.json().get("response", "")
    else:
        return f"Error: {response.status_code} - {response.text}"
