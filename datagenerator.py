import random
import string
import datetime
print("1: REAL\n"
      "2: CHAR\n"
      "3: INTEGER\n"
      "4: STRING\n"
      "5: BOOLEAN\n"
      "6: DATE\n"
      )
a = string.ascii_letters + string.digits
bool= ["TRUE","FALSE"]
input= int(input("input number"))
if input == 1:
    print(random.uniform(0,100))
if input ==2:
    print(random.choice(a))
if input ==3:
    digit= string.digits
    print(int(random.choice(digit)))
if input == 4:
    d= ''.join((random.choice(a)) for i in range(10))
    print(d)
if input ==5:
    print(random.choice(bool))
if input== 6:
    x= random.randint(1980,2020)
    y= random.randint(1,12)
    z= random.randint(1,30)
    print(datetime.datetime(x,y,z))

