import os
import json
from dotenv import load_dotenv
from ai import AzureOpenAI

# Cargar variables de entorno
load_dotenv()

endpoint = os.getenv("ENDPOINT_URL")
deployment = os.getenv("DEPLOYMENT_NAME")
api_key = os.getenv("AZURE_OPENAI_API_KEY")

# Verificar las variables de entorno
print(f"ENDPOINT_URL: {endpoint}")
print(f"DEPLOYMENT_NAME: {deployment}")
print(f"API Key: {api_key}")

# Crear la instancia de AzureOpenAI
ai_client = AzureOpenAI(api_version="2024-05-01-preview", api_key=api_key, endpoint=endpoint)

def send_prompt_to_AzureOpenAI(prompt_message):
    chat_prompt = [
        {"role": "system", "content": "Sos un asistente de IA"},
        {"role": "user", "content": prompt_message}
    ]
    
    response = ai_client.send_chat_request(model=deployment, messages=chat_prompt)
    
    # Guardar respuesta en un archivo JSON
    with open("response.json", "w", encoding="UTF-8") as f:
        json.dump({"response": response}, f, indent=4, ensure_ascii=False)

    return response
