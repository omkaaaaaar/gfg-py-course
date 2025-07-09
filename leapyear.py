# Take year input and print if year is a leap year
year=int(input("Enter a year: "))
if year%4==0 and year%100!=0:
    print("True")
elif year%400==0:
    print("True")
else:
    print("False")