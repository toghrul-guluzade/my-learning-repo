

n = int(input())

string = []

for num in range (0, n):
  word = input()
  string.append(word)

for word in string:
  length = int(len(word))
  if length >= 10:
    print(word[0], (length - 2), word[length - 1], sep="")
  else:
    print(word)

