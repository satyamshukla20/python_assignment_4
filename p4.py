#Create a program to check eligibility of the person for loan  with the help of oops concepts and exception handling. Person whose salary is less than 10K/ Month will not be eligible for the loan.

class customExceptionHandler(Exception):
    pass

class Person:
    def __init__(self,name,income) -> None:
        self.name=name
        self.income=income

    def eligible(self):
        if self.income<=10000:
            raise customExceptionHandler("the income is not sufficient to avial the loan")
        return "You can avail loan"

    
    print("Hello, Can I know your name?")
name=input()
print("what's your Monthly Salary")
salary=int(input())

p=Person(name,salary)
try:
    print(p.eligible())
except customExceptionHandler as e:
    print(e)




    