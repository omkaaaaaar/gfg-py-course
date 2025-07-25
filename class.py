#Basic def/Function example
def func():
    print("This is a function in class.py")

print()
print("Before func() is called")    
func()
print("After func() is called")
print()


#Date print/ simple example
def printDate(d,m,y):
    print(d,m,y, sep="-")

print("My Birthday is on:")
printDate("19","09","2025")    
print()


#DATE Return example
def getDate(d, m, y):
    return d+"-"+m+"-"+y

print("India got independence on")
d = getDate("15","08","1947")
print(d)

