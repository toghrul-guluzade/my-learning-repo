import string


password = input("Enter your Password: ")


upperCase = [1 if c in string.ascii_uppercase else 0 for c in password]
lowerCase = [1 if c in string.ascii_lowercase else 0 for c in password]
special = [1 if c in string.punctuation else 0 for c in password]
digits = [1 if c in string.digits else 0 for c in password]
length = len(password) 



with open('python\common_passwords.txt', 'r') as file:
  common_passwords = file.read()

if password in common_passwords:
  print("Password found in common passwords!")
  exit()

if length < 8:
  print("Password length must be at least 8 characters.")
  exit()

if sum(upperCase) == 0:
  print("Password must include at least one uppercase letter.")
  exit()
  
if sum(lowerCase) == 0:
  print("Password must include at least one lowercase letter.")
  exit()
  
  
if sum(digits) == 0:
  print("Password must include at least one digit.")
  exit()


score = 0

if sum(upperCase) > 1:
  score += 1

if sum(lowerCase) > 1:
  score += 1

if sum(special) >= 0:
  score += 1

if sum(special) >= 2:
  score += 2

if length >= 8:
  score += 1

if length >= 9:
  score += 1

if length >= 10:
  score += 1

print("The score of your password is ", score, "/8")


  
  
  
  
  
