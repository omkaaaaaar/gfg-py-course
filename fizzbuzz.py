#User function Template for python3
a=int(input("Enter a number:"))
if a%3==0 and a%5==0:
  print("FizzBuzz")
elif a%3==0:
  print("Fizz")
elif a%5==0:
  print("Buzz")    
else:
  print(a)    