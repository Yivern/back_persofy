from cryptography.fernet import Fernet

with open("image.txt", "rb") as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

# Ejemplo de encriptado
config_data = {

    "yt_options": {
        "format": "bestaudio/best",
        "noplaylist": True,
        "quiet": True,
        "default_search": "ytsearch",
    },
}

encrypted_config = {}
for key, value in config_data.items():
    encrypted_config[key] = {
        k: cipher_suite.encrypt(str(v).encode()).decode()
        if isinstance(v, str) else v
        for k, v in value.items()
    }

with open("config.py", "w") as file:
    file.write(f"ENCRYPTED_CONFIG = {encrypted_config}")

print("Encrypted credentials saved to config.py.")
