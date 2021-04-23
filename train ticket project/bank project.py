import pymysql
db = pymysql.connect(host="localhost", user='root', password='', database='parthiban')

print('welcome to the canarabank')

class user:
    def __init__(self,amount):
        self.amount = 0

    def userdetails(self):

        print("name:", name)
        print("age:", age)


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

    x = db.cursor()
    x.execute("use parthiban")
    try:
        x.execute("create table bankdetails(name varchar(30), age int,phoneno int,email varchar(20))")
    except Exception as e:
        print(e)

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    phoneno = int(input("enter your phone number"))
    email = input("enter your email id:")

    x.execute("INSERT into bankdetails(name,age,phoneno,email) VALUES (%s,%s,%s,%s)", (name,age,phoneno,email))
    db.commit()
    x.execute("select * from bankdetails")
    
    c = x.fetchall()
    print(c)
    db.close()

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

