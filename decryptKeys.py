from cryptography.fernet import Fernet

# Load the secret key from the .env file
with open(".env", "r") as env_file:
    for line in env_file:
        parts = line.strip().split(":")
        if len(parts) == 2:
            key, value = parts
            if key == "SECRET_KEY":
                secret_key = value.encode()
                break
    else:
        # Handle the case where SECRET_KEY is not found
        print("SECRET_KEY not found in .env file")
        exit(1)

cipher_suite = Fernet(secret_key)

def retrieveKeys():
    # Retrieve and decrypt access key and secret
    with open(".env", "r") as env_file:
        for line in env_file:
            parts = line.strip().split(":")
            if len(parts) == 2:
                key, value = parts
                if key == "ENCRYPTED_ACCESS_KEY":
                    decrypted_access_key = cipher_suite.decrypt(value.encode()).decode()
                elif key == "ENCRYPTED_SECRET":
                    decrypted_secret = cipher_suite.decrypt(value.encode()).decode()

    return decrypted_access_key, decrypted_secret
    #print("Decrypted Access Key:", decrypted_access_key)
    #print("Decrypted Secret:", decrypted_secret)

    # Now you can use decrypted_access_key and decrypted_secret for your API calls
