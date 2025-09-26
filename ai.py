from openai import OpenAI

class AzureOpenAI:
    def __init__(self, api_version, api_key, endpoint):
        self.client = OpenAI(
            api_key=api_key,
            base_url=endpoint
        )
        self.api_version = api_version

    def send_chat_request(self, model, messages, temperature=0.7, max_tokens=800):
        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
