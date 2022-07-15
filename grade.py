# WAP to print grade of a number on basis of percentage.
# a. If per greater than or equal to 75 @A grade
# b. If per between 60-75@ B grade
# c. If per between 50-60@ C grade
# d. If per between 40-50@ D grade
# e. If per less than 40 @Fail
per = int(input("Enter the percentage of a student: "))
if per >= 75:
    print("Grade A")
elif 60 <= per:
    print("Grade B")
elif 50 <= per:
    print("Grade C")
elif 40 <= per:
    print("Grade D")
else:
    print("Fail")
