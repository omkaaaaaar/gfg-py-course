n=int(input("Enter n:"))
if (n<=1):
    print("Not a prime number")
else:
    for i in range(2, n):
        if(n%i==0):
            print("Not a prime number")
            break    
    else:
        print("Prime number")
