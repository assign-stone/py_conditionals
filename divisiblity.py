# WAP to check if a given number is divisible by 3, 4 and 8 or not.
num = int(input("Enter any number: "))
if num % 3 == 0 and num % 4 == 0 and num % 8 == 0:
    print("Divisible by all three")
else:
    print("Not Divisible by all three")
