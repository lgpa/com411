print("Where should I look?")
look = input()

if(look=="in the bedroom"):
 print("Where in the bedroom should I look?")
 look = input()
 if(look=="under the bed"):
    print("Found some shoes but no battery")
  else:
    print("Found some mess but no battery")
elif(look=="in the bathroom"):
  print("Where in the bathroom should I look?")
  look=input()
  if(look=="in the bathtub"):
    print("Found a rubber duck but no battery")
  else:
    print("Found a wet surface but no battery")
elif(look=="in the lab"):
  print("Where in the lab should I look?")
  look=input()
  if(look=="on the table"):
    print("Yes! I found my battery!")
  else:
    print("Found some tools but no battery")
else:
  print("I do not know where that is but I will keep looking")
 