import os
from cryptography.fernet import Fernet

# Generate a secret key for encryption
secret_key = Fernet.generate_key()
cipher_suite = Fernet(secret_key)

# Your Alibaba Cloud access key and secret, delete after operation done
access_key = ""
secret = ""

# Encrypt access key and secret
encrypted_access_key = cipher_suite.encrypt(access_key.encode())
encrypted_secret = cipher_suite.encrypt(secret.encode())

# Save the encrypted values in a .env file
with open(".env", "w") as env_file:
    env_file.write(f"ENCRYPTED_ACCESS_KEY:{encrypted_access_key.decode()}\n")
    env_file.write(f"ENCRYPTED_SECRET:{encrypted_secret.decode()}\n")
    env_file.write(f"SECRET_KEY:{secret_key.decode()}\n")

print("Access key and secret encrypted and saved in .env")
