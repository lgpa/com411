print("What phrase do you see?")
phrase=input()
rev = ""
for letter in phrase:
  rev=letter + rev

print(rev)