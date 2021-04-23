n = ['parthiban']
p = ['12345']

newuser = int(input("select 2 new account or 1 existing user"))


if newuser == 2:

    name =input("enter your name:")
    password =input("enter your password")

    if name in n:
        print("alredy existed")
    else:
         n.append(name)
         p.append(password)
         print("created sucessfully")
         print(n)
         print(p)

         a= dict(zip(n,p))

         name= input('enter your username:')
         password= input('enter your password:')
         if name in a.keys()and password in a.values():
             print('login sucessfully')
         else:
             forgot=input("forgot your password y/n:")
             if forgot== 'y':
                 new =input("enter your new password:")
                 a[name]=new
                 if name in a.keys():
                     name = input("enter your name:")
                     password=input("enter your password:")
                     if [name] == password:
                         print("password changed sucesfully:")
                         print(a)
                     else:
                         print("enter your password again:")

else:
    name= input("enter your name:")
    password=input("enter your password:")
    if name in n:
        print("good login sucessfully:")
    else:
        print("your password and user name wrong")











