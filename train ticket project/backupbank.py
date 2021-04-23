import re

from numpy import random

print('welcome to the canarabank')

class user:
    def __init__(self,amount):
        self.amount = 0

    def userdetails(self):
        print("name:", name)
        print("age:", age)
        print("phone number:", phoneno)








class bank(user):
    def __init__(self,amount):


        super().__init__(amount)
        self.a = self.amount

    def deposite(self):
        dep = int(input("enter your deposite cash amount"))
        self.a = self.a + dep
        print(self.a)
        print("deposited sucessfully")
        existingure = int(input("3 deposite: 4 withdrawl: 5 check_balance: 6 exit:"))

        if existingure == 3:
            x.deposite()

        if existingure == 4:
            x.withdrawl()

        if existingure == 5:
            x.checkbalance()

        if existingure == 6:
            print("exit")

    def withdrawl(self):
        withdrl = int(input("enter the withdrawl amount:"))
        if self.a >= withdrl:
            self.a = self.a - withdrl
            print(self.a)
        else:
            print("insufficant banlance")
        print("withdrawl sucesfully")
        existinguser = int(input("3 deposite: 4 withdrawl: 5 checkbalance: 6 exist:"))

        if existinguser == 3:
            x.deposite()

        if existinguser == 4:
            x.withdrawl()

        if existinguser== 5:
            x.checkbalance()

        if existinguser == 6:
            print("exit")

    def checkbalance(self):
        print("your balance is:",self.a)
        existinguser = int(input("3 deposite: 4 withdrawl: 5 checkbalance: 6 exist:"))

        if existinguser == 3:
            x.deposite()

        if existinguser == 4:
            x.withdrawl()

        if existinguser == 5:
            x.checkbalance()

        if existinguser == 6:
            print("exit")

newuser = int(input("select 1 new account or 2 existing user"))

if newuser==1:
    print("please fill your details:")
    name = (input("enter your name:"))
    if name<="a":
        x = re.search("^[A-Z]{1}[a-z]{30}$",name)
    else:
         print("invalid name please enter your first letter in uppercase")
    age = (input("enter your age:"))
    phoneno =(input("enter your phoneno:"))
    if re.findall(r'[567]/d{10}$',phoneno):
        print(phoneno)
    else:
        print("enter your 10 digit phoneno")
    print("your account no is-")
    print(random.randint(9,size=8))
    print("your canarabank account is sucessfully created")

else:
     print("continue")

x = bank(0)

existinguser = int(input("3 deposite: 4 withdrawl: 5 checkbalance: 6 exist:"))

if existinguser == 3:
    x.deposite()

if existinguser == 4:
    x.withdrawl()

if existinguser == 5:
    x.checkbalance()

if existinguser == 6:
    print("exist")