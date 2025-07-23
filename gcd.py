#Normal GCD
a=int(input("Enter a: "))
b=int(input("Enter b: "))
small=min(a,b)
for i in range(1,small+1):
  if(a%i==0 and b%i==0):
    res=i
print("The GCD of", a, "and", b, "is:", res)    

#Gcd with math module
import math
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
gcd=math.gcd(a,b)
print("The GCD of", a, "and", b, "is:", gcd)