vowel = ["a","e","i","o","u","A","E","I","O","U"]
c=''
build = ''
print("input a sentence or word you want to be converted")
string = input()
for i in string:
    if i not in vowel:
        build+= i +"o" +i
    else:
        build+=i


print(build)


