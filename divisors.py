#for loop
n=int(input("Enter n: "))
for i in range(1,n+1):
    if(n%i==0):
        print(i)


#while loop
n=int(input("Enter n: "))
x=1 #initialisation/declaration
while x<=n: #condition check
    if(n%x==0):
        print(x)
    x=x+1 #incrementation (decrementation if needed in some problems)
