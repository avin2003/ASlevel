#Can you create a randomly generated password based off a
#  favorite color, place and animal? And also add special
# characters to the end of it.
import random

symbols= ['!','@','#','$',"%"]
list= []
build= ''
favcolour = input("input you fav colour")
list.append(favcolour)
animal = input("input your fav animal")
list.append(animal)
place= input("input ur fav place")
list.append(place)

password = ''.join(random.sample(list,3))
for i in range(3):
    s= random.choice(symbols)
    build+= s
print("password is", password+build)

