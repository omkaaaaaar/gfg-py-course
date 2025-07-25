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


#Variable Length Arguments
def sum(*elements):
    res=0
    for x in elements:
        res += x
    return res

print(sum(10,20))    
print(sum(10,20,30))
print(sum(10))
print(sum())