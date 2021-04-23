import pymysql


db = pymysql.connect(host="localhost", user='root', password='', database='parthiban')


x = db.cursor()
x.execute("use parthiban")
try:
    x.execute("create table bix(name varchar(30), age int) ")
except Exception as e:
    print(e)

name = input("Enter your name: ")
age = int(input("Enter your age: "))

x.execute("ALTER TABLE bix MODIFY age varchar(20)")
db.commit()
x.execute("select * from bix")
c = x.fetchall()
print(c)
db.close()