num = int(input("Enter a number: "))

if num % 2 == 0:
  print(f"{num} is even")

if num % 5 == 0:
  print(f"{num} is divisible by 5")
else:
  print(f"{num} is not divisible by 5")  

if num % 2 != 0:
  print(f"{num} is odd") 
