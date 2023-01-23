#Create a program to validate the age of the voter with the help of custom exception. Voters whose age is less than 18 should not be allowed to vote.

class customExceptionHandler(Exception):
    pass

def Validation(age):
    if age<18:
        raise customExceptionHandler("the age is less than the minimum criteria to vote!");
    return "You are allowed to vote!"


print("provide the age of the voter")
age=int(input())
try:
    print(Validation(age))
except customExceptionHandler as e:
    print(e)


    