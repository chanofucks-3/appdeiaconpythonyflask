import os

keys_to_check = ["ENDPOINT_URL", "DEPLOYMENT_NAME" ,"AZURE_OPENAI_API_KEY"]

for key in keys_to_check:
    print(f"{key}: {os.getenv(key)}")
    
print("\nTodas las variables de entorno:")
for key, value in os.environ.items():
    print(f"{key}: {value}")