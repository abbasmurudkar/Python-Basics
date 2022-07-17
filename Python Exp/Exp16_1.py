# Practical no 16
a = int(input("Enter the Divisible Number: "))
b = int(input("Enter the First Number: "))
c = int(input("Enter the Second Number: "))
try:
    q = a / (b-c)
    print(q)
except ZeroDivisionError:
    print("The Number Cannot Be Divisible By Zero")

class check_pass(Exception):
    pass
try:
    pswd = "1234"
    a = input("Enter the password: ")
    if(a == pswd):
        print("The Password Is Correct")
    else:
        raise check_pass
except check_pass:
    print("The Given Password is Invalid")
