number = 5
while number <= 10:
    print(number)
    number = number + 1



jack = 'write a poem!\n'
jack +='enter "esc" to end\n'

poem = "that is a slap of close set"
line = "this is nice to atten"

while line!='esc':

     line = input(jack)
     if line =='esc':
         continue
     poem += line
     poem += '\n'


print(poem.replace('esc',''))
















#month = int (input('enter a month (as a integer)'))
#day = 1
#while  day <= 31:
    #if month == 2 and day > 28:
     #   break
    #if ( month == 4  or month == 6) and day > 30:
        #day += 1
       # continue
      #print(day)
     # day += 1




pets =['dogs','cat','dogs','rabbits','elephants']

print(pets)
while 'cat' in pets:
    pets.remove('cat')









