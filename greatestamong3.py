# WAP to find greatest number among 3 given numbers.

no1 = int(input("Enter 1st number: "))
no2 = int(input("Enter 2nd number: "))
no3 = int(input("Enter 3rd number: "))
if no1 > no2:
    if no1 > no3:
        print("no1 is greatest")
    else:
        print("no3 is greatest")
elif no2 > no3:
    print("no2 is greatest")
else:
    print("no3 is greatest")
