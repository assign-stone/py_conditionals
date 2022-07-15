# WAP in following pattern and calculate result
# 1 For addition            Enter choice
# 2 For subtraction          2
# 3	For division            Enter 2 numbers
# 4	For modulus              10    4
#                           Subtraction= 6

num = int(input("Enter number 1 for Addition, 2 for Subtraction,3 for Division, 4 for Modulus: "))
if num == 1:
    print("Addition")
    a = int(input("Enter 1st value: "))
    b = int(input("Enter 2nd value: "))
    c = a + b
    print(c)
elif num == 2:
    print("Subtraction")
    d = int(input("Enter 1st value: "))
    e = int(input("Enter 2nd value: "))
    f = d - e
    print(f)
elif num == 3:
    print("Division")
    g = int(input("Enter 1st value: "))
    h = int(input("Enter 2nd value: "))
    i = g / h
    print(i)
else:
    print("Modulus")
    j = int(input("Enter 1st value: "))
    k = int(input("Enter 2nd value: "))
    m = j % k
    print(m)



