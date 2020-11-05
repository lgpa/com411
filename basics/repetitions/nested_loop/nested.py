print("How many rows should I have?")
rows=int(input())
print("How many columns should I have?")
colums=int(input())
for row in range(0,rows,1):
  for colum in range(0,colums,1):
    print(".|.", end="")
  print()

print("done")