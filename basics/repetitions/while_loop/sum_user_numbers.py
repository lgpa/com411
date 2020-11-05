print("How many numbers should I sum up?")
numbs=int(input())
total=0
count=0
while(count<numbs):
  count=count+1
  print("enter the {} number of {}".format(count,numbs))
  add=int(input())
  total=total+add

print("the total value is {}".format(total))