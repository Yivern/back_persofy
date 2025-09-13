from cryptography.fernet import Fernet

key = Fernet.generate_key()

print(f"Save the secure key: {key.decode()}")
