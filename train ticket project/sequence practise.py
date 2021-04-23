languages = ['python','java','mysql','javascript','html','c++']
fav ='python'

print(len(languages))
print(len(fav))

print(languages[2])
print(fav[-2])


print(fav[len(fav)-1])

print(languages[4])

print(languages[:])
print(fav[:])

print(fav*2)
print(languages*5)
print(languages)

print(fav +'languages')
print(languages +['go','R'])
print(languages)

p_list = list(fav)
print(p_list)

print(''.join(p_list))
print(p_list)


print('-'.join(p_list))
print(','.join(languages))

print(languages.index('java'))
print('python' in languages )