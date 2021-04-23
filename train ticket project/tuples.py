languages = ['python,','my sql']
languages.append('django')
print(languages)

name = 'my sql'

name = name.replace('m','q')
print(name)

locations =(45.0025255,55.899600)


print(f'latitude: {locations[0]}')
print(f'longitude: {locations[1]}')



locations =(10,20)
print(locations)



map = [(25,75),(35,55),(88,99)]
for coordinates in map:
    for position in coordinates:
        print(position)

a =(10)
print(type(a))

b = (10,)
print(type(b))

beta =('a','b','c','d','e')
print(beta +('f','g'))
print(beta*3)
print((beta[:3]))
print(beta.index('a'))
print((1,2,3,4,5,2,2,2,2,6).count(2))


