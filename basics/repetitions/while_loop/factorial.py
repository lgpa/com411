print("Please enter a number:")
num=int(input())
count=0
total=1
while(count<num):
  count=count+1
  total=total * count

print("the factorial is {}".format(total))
