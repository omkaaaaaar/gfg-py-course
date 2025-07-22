#This code calculates the factorial of a number n

#Method 1
n = int(input("Enter n:"))
res=1
for i in range(2, n+1):
    res=res*i
print("Factorial of", n, "is", res)



#Method 2
import math
n=int(input("Enter n:"))
res=math.factorial(n)
print("Factorial of", n, "is", +res)                      