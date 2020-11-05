print("How many bars should be charged?")
bars=int(input())
count=0
while(count<bars):
  count=count+1
  print("charging: ", "█ " * count)
  

print("The battery is fully charged.")