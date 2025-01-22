from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.identity import ClientSecretCredential
from dotenv import load_dotenv
import os
load_dotenv('.env')

# Replace with your Key Vault URL
key_vault_url = os.getenv('KEY_VAULT_DOMAIN')
client_id = os.getenv('CLIENT_ID')
tenant_id = os.getenv('TENANT_ID')
client_secret = os.getenv('CLIENT_SECRET')

# Authenticate using DefaultAzureCredential
credential = ClientSecretCredential(client_id=client_id, tenant_id=tenant_id, client_secret=client_secret)

# Create a SecretClient
client = SecretClient(vault_url=key_vault_url, credential=credential)

# Replace with the name of the secret you want to retrieve
secret_name = os.getenv('SECRET_NAME')

try:
    # Retrieve the secret
    secret = client.get_secret(secret_name)
    print(f"Secret Value: {secret.value}")
except Exception as e:
    print(f"Error retrieving secret: {e}")
