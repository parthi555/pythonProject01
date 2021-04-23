import datetime
from numpy import random
print('happyjourney')
current_date_time = datetime.datetime.now()
print(current_date_time)
train_no = random.randint(9,size=(5))
print('train_no:',train_no)

area = {'chengalpattu': 1, 'paranur': 2, 'singaperumal': 3, 'kovil': 4, 'maraimalai nagar': 5, 'kattangulattur': 6,
        'potheri': 7, 'guduvancheri': 8, 'Urappakkam': 9, 'Vandalur': 10, 'Perungulattur': 11, 'tambaram': 12,  'Chrompet': 13,
        'pallavarm': 14, 'tirusulam': 15, 'minambakkam': 16, 'palavanthangal': 17, 'st Thomas Mount': 18,
        'guindy': 19, 'saidapet': 20, 'mambalam': 21, 'kodambakkam': 22, 'nungambakkam': 23, 'chetpet': 24,
        'egmore': 25, 'park': 26, 'fort': 27, 'mearina beach': 28, 'basent bridge': 29}

s = input('enter your starting point')
d = input('enter your destination reach')
price = 10
i = area[s]
j = area[d]
x = j - i
a = 10

if x <16:
     print(price)

else:
    c = price + 20
    print(c)














