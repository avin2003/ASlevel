nn= input("input first number less than 100")
mm= input("input second number less than 100")

n1= nn[0]
n2= nn[1]
m1= mm[0]
m2= mm[1]


row = int(n1) * int(m1)
column= int(n2) * int(m2)
checkboard= []
even= ["#"]*column
odd= ["#"]*column
for i in range(len(even)):
    if i%2 ==0:
        even[i] = "."
    else:
        even[i] = "*"

for i in range(len(odd)):
    if i%2 ==0:
        odd[i] = "*"
    else:
        odd[i] = "."

for i in range(row):
    if i%2==0:
        checkboard.append(even)
    else:
        checkboard.append(odd)

for i in range(len(checkboard)):
    print(checkboard[i])










