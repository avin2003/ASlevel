characters= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t''u','v','w','x','y','z']
u_characters= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T''U','V','W','X','Y','Z']
numbers= ['0','1','2','3','4','5','6','7','8','9']
symbols= ['!','@','#','$','%','&']

build = ''
import random

for i in range(0,30):
    c = random.choice(characters)
    uc= random.choice(u_characters)
    n= random.choice(numbers)
    s= random.choice(symbols)
    build = build + c +uc + n + s

print(build)
 
