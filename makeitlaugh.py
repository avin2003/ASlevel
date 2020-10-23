a=""
build= ''
make_it_laugh= input("input sentence")
vowel = ["a","e","i","o","u","A","I","E","O","U"]
for i in make_it_laugh:
    if i in vowel:
        build += "haha"
    else:
        build+= i

print(build)




