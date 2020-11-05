print("enter the first number")
num1 = int(input())
print("enter the second number")
num2 = int(input())
print("enter the third number")
num3 = int(input())

even = 0
odd = 0

if(num1 % 2) == 0:
  even = even +1
else:
  odd = odd +1

if(num2 % 2) == 0:
  even = even +1
else:
  odd = odd +1

if(num3 % 2) == 0:
  even = even +1
else:
  odd = odd +1

print("there are {} even numbers and {} odd numbers".format(even,odd))