import datetime

x= int(input("input first full year"))
y= int(input("input first month"))
z= int(input("input first day"))

a= int(input("input second full year"))
b= int(input("input second month"))
c= int(input("input second day"))

first= datetime.datetime(x,y,z)
second= datetime.datetime(a,b,c)

difference = (second -first)
print("difference in day is",difference)
