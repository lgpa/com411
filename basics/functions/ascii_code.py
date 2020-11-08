print("Program Started!")
print("Please enter a standard character:")
letter=input()
if(len(letter)<2):
  print("The ASCII code for {} is {}".format(letter,ord(letter)))
else:
  print("there can be only one charater")
print("Program Ended!")
