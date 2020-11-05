print("What level of brightness is required?")
level=int(input())
for count in range(2,level+1,2):
  print("Beep's brightness level: ","* "*count)
  print("Bop's brightness level: ","* "*count)

print("Adjustments complete!")