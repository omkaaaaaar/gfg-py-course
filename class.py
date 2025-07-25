def func():
    print("This is a function in class.py")

print("Before func() is called")    
func()
print("After func() is called")


#DATE
def getDate(d, m, y):
    return d+"-"+m+"-"+y
print("India got independence on")
d = getDate("15","08","1947")
print(d)