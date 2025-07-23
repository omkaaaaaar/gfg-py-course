a=int(input("Enter a: "))
b=int(input("Enter b: "))
res=max(a,b)
while(res<=a*b):
    if (res%a==0 and res%b==0):
        break
    res+=1
print("The LCM of", a, "and", b, "is:", res)

#
import math
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
lcm=math.lcm(a, b)
print("The LCM of", a, "and", b, "is:", lcm)