name = ['parthi']
password = ['12345']
age = 23
otp = 555
number = int(input("enter the no"))
while age < number:
    name = input('enter a name:')
    password = input('enter a password:')

    if name in name:
         print('alredy exist')
    else:
        name.append(name)
        password.append(password)
        number -=1
        print('created sussesfully')
        print(name)
        print(password)
a = dict(zip(name,password))
print(a)
login = input('do you want to login yes/no')
if login == 'yes':
    username = input('enter your name:')
    userpassword = input('enter your password')
    if username in a.keys() and userpassword in a.values():
        print('sucessfully')

    else:
        print('does not match')

forget = input('forgot your password yes/no')

if forget == 'yes':
    print('enter your otp')
    print(otp)
    mobile = int(input('enter your otp'))
    if otp == mobile:
        new = input('enter your new password:')
        a[username] = new
        if username in a.keys():
            username = input('enter your user name')
            password = int(input("enter your password"))
            if a[username] == password:
                print('sucessfully changed password')
        print(a)
else:
    print('welcome to bix')















