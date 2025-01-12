import os
from cryptography.fernet import Fernet


files = os.listdir()

with open("key.txt", "rb") as file:
  key = file.read()
  

for file in files:
  if file == "key.txt" or file == "encrypt.py" or file == "decrypt.py" or file == "__pycache__":
    continue
  with open (file, "rb") as f:
    data = f.read()
    decrypt = Fernet(key).decrypt(data)
  with open(file, "wb") as f:
    f.write(decrypt)
    print("Files {files} decrypted successfully")