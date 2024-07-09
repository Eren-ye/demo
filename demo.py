# print(" hello")
# x=10
# y=20
# if x>y:
#     print(f" so{x}")
# else:
#   print(f" so{y}")

# a=10
# b=20
# c=30
# if a>b and a>c:
#    print(f"a is greater")
# elif b>a and b>c:
#    print(f" b is greater")
# elif c>a and c>b:
#    print(f"C IS GREATER")
# else:
#    print(f"all are equal")


# a=int(input(" Enter the 1st subject marks"))
# b=int(input(" Enter the 2nd subject marks"))
# c=int(input(" Enter the 3rd subject marks"))
# d=int(input(" enter the 4th subject marks"))
# e=int(input(" enter the 5th subject marks"))

# per = (a+b+c+d+e)/500*100
# print(f" total percentage is :{per}")

# if per>=75 and per<=100:
#    print(" grade A")
# elif per>=60 and per<75:
#     print(" grade B")
# elif per>=45 and per<60:
#    print(" grade C")
# elif per>=35 and per<45:
#     print(" grade D")
# else:
#     print(" grade F")

# age=int(input(" Enter your age: "))
# if age<18:
#     print(" you are child")
# elif age>=18:
#     if age>=18 and age<=60:
#         print(" you are eligible to vote")
#     else:
#         print(" You are old")

pin=int(input("Enter the PIN :"))
if pin==1234:
    print(" Welcome to ATM")
    print(" 1. Balance Enquiry")
    print(" 2. Withdrawal")
    option=int(input("Enter your option :"))
    if option==1:
        print(" Your balance is 10000")
    elif option==2:
        print(" Enter the amount to withdraw :")
        amount=int(input("Enter the amount :"))
        if amount>10000:
            print(" Insufficient balance")
        else:
            print(f" Your preveious balance is 10000 and current amount is {10000-amount}")
    else:
        print(" Invalid option")
else:
    print(" Invalid PIN")
