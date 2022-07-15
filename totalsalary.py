# WAP to calculate total salary based on basic salary. Total salary will be calculated as addition of
# basic salary,ta (travelling allowance), and hra (house rent allowance).
# So,first find out ta and hra based on following criteria:

# a.If BS in between 4000-6000 @ta 40% & hra is 20%
# b.If BS in between 6000-10000 @ta 45% and hra 20%
# c.If BS is greater than 10000 @ta 55% and hra is 5000.

basic_salary = int(input("Enter your basic salary: "))
if 4000 <= basic_salary:
    ta = 0.4 * basic_salary
    hra = 0.2 * basic_salary
elif 6000 <= basic_salary:
    ta = 0.45 * basic_salary
    hra = 0.2 * basic_salary
elif 10000 <= basic_salary:
    ta = 0.55 * basic_salary
    hra = 5000
else:
    print("Not Applicable")

# print("ta = ", end="")
# print(ta)
# print("hra = ", end="")
# print(hra)
total_salary = basic_salary + int(ta) + int(hra)
print("Total Salary = ", end="")
print(total_salary)
