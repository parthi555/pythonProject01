languages = ['python','java','mysql','javascript','html','c++']
print(languages)
print(languages[3].upper())
print(languages[3])

languages[2] ='sql'
print(languages)

languages.append('django')
print(languages)

languages.extend(['php','css'])
print(languages)
languages.append(['php','css'])
print(languages)

del languages[-1]
print(languages)


languages.insert(6,'framework')
print(languages)

removed_language = languages.pop()
print(removed_language)
print(languages)

html = languages.pop(-5)
print(html)

languages.remove('java')
print(languages)

languages.sort()
print(languages)

languages.sort(reverse=True)
print(languages)

print(sorted(languages))
print(languages)

numbers =[10,20,30,40,50,3,10001,8]
numbers.reverse()
print(numbers)







