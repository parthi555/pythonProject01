import re

a = "welcome to BIX IT ACADEMY"
x = re.split('\s',a)
print(x)

x = re.split('\s',a,3)
print(x)
x = re.sub('\s','#',a,2)
print(x)

x = re.search('o',a)
print(x.span())
print(x.string)
print(x.groups())

x = re.findall("A",a)
print(x)


list = ['7339228061','9791503380,9840265894,7871597969']
for record in list:
    if re.match(r'[789]\d{9}',record):
         print(record)