#Default Arguments in Python
def printDetails(id,name="NA", price="NA"):
    print(f"ID is {id}")
    print(f"Name is {name}")
    print(f"Price is {price}")

printDetails(101, "Laptop", 50000)
print()
printDetails(102, "Mobile")
print()
printDetails(103)  # Only ID provided, others will be default "NA"
print()
print("----------------------------")
print()

#Variable Length Arguments Tuple Based, Only values
def sum(*elements):
    res=0
    for x in elements:
        res += x
    return res

print(sum(10,20))    
print(sum(10,20,30))
print(sum(10))
print(sum())
print()
print("----------------------------")
print()

#Function with Default and Variable Length Arguments - Dictionary Based, Key-Value Pairs
def printDetails(**details):
    for key, value in details.items(): # unpacking the dictionary, basically items that are stored in details
        print(f"{key} is {value}")

printDetails(ID=101, Name="Laptop", Price=50000)
print()
printDetails(ID=102, Name="Mobile")
print()
printDetails(ID=103)  # Only ID provided, others will be default "NA"