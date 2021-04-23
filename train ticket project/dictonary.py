person ={
    'name': 'parthiban',
    'age' : 23

}

print(person['name'])
print(person['age'])

person['age'] = 22
print(person)

person['proffesion'] = 'developer'
print(person)

del person['proffesion']
print(person)

person['locations'] = (13.8854,15.258)
person['locations'] = {
    'area': 'royapetha',
     'street':'balaji nagar',
    'city': 'chennai'


}

print(person)


person['languages'] =['python','my sql','djsngo']
print(person)

for key in person.keys():
    print(key)

for value in person.values():
   print(value)

for key,value in person.items():
    print(f'{key.title()} = {value}')

    print('lopoping through complex dictionary')

for key,value in person.items():
    if isinstance(value,tuple) or isinstance(value,list):
        for item in value:
            print(f'\t {item}')
    elif isinstance(value,dict):
        print(key)
        for key2, value2 in value.items():
            print(f'\t {key2} = {value2}')
        else:
            print(f'{key} ={value}')
            print()