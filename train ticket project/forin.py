#language = ['python','mysql','java','javascript','html','css']

#for language in language:
 #   print(language)

#language = 'python'
#for char in language:
 #   print(char)

bikes = ['cbr','bmw','ktm','royalenfield']
for bike in bikes:
    if bike == 'bmw':
        print(bike.upper())
    else:
     print(bike.title())


chicken_rice = 100

requested_toppings = ['onion','tomatosaurse']
for requested_topping in requested_toppings:
    if requested_topping == 'omlet':
        chicken_rice += 200
    else:
        chicken_rice += 150
        print(f'chicken rice: {chicken_rice}')

