for i in range(1, 1*10+1,1):
    print(i, end=" ")
print() # prints a newline / Starts a new line    
for i in range(2,2*10+1,2):
    print(i, end=" ")
print()
for i in range(3,3*10+1,3):
    print(i, end=" ")
print()

n=int(input("Enter n: "))
m=int(input("Enter m: "))
for i in range(n, n*m+1,n):
    print(i, end=" ")
print()    

for i in range(1,11):
    for j in range(i, i*10+1, i):
        print(j, end=" ")
    print()    

# This code generates the multiplication table for a given number n up to m times.   