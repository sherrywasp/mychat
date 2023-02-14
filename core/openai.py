import json
import requests
from settings import Settings


class OpenAI:

    def __init__(self):
        self.api_url = 'https://api.openai.com/v1/completions'
        self.settings = Settings()

    def completions(self, prompt: str):

        # 读取API_KEY
        with open('api_key.txt') as f:
            api_key = f.read()

        headers = {
            'Authorization': 'Bearer '+api_key
        }
        body = {
            "model": "text-davinci-003",
            "prompt": prompt,
            "temperature": 0.6,
            "max_tokens": 2048
        }

        res = requests.post(self.api_url, headers=headers, json=body)
        res_json = res.json()
        print(json.dumps(res_json, indent=4))   # 响应日志
        if res.status_code == 200:
            return res_json["choices"][0]["text"]
        else:
            raise Exception(self.settings.exception_msg)
