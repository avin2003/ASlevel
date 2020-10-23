total=0
while True:
    isbn= input("input isbn number")
    if len(isbn) != 13:
        isbn= input("input isbn number")
    else:
        break
for i in isbn[1::2]:
    x= int(i) *3
    total= total +(x)
for i in isbn[0:12:2]:
    total = total + (int(i))

cd = total%10
print(cd)
if cd == 0:
    checkd = 0
else:
    checkd = 10- cd
print(checkd)







