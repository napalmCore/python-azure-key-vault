from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.identity import ClientSecretCredential


# Replace with your Key Vault URL
key_vault_url = "<your-azure-key-vault-domaine>"
client_id = "<client-id>"
tenant_id = "<tenant-id>"
client_secret = "<client-secret>"

# Authenticate using DefaultAzureCredential
credential = ClientSecretCredential(client_id=client_id, tenant_id=tenant_id, client_secret=client_secret)

# Create a SecretClient
client = SecretClient(vault_url=key_vault_url, credential=credential)

# Replace with the name of the secret you want to retrieve
secret_name = "test-secret"

try:
    # Retrieve the secret
    secret = client.get_secret(secret_name)
    print(f"Secret Value: {secret.value}")
except Exception as e:
    print(f"Error retrieving secret: {e}")
