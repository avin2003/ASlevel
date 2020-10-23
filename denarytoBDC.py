BCD= ["0000", "0001", "0010", "0011","0100","0101",'0110','0111','1000','1001' ]
build = ''

decimal = input("input decimal")

for i in decimal:
    if i == "0":
        build += BCD[0]
    elif i == "1":
        build += BCD[1]
    elif i == "2":
        build += BCD[2]
    elif i == "3":
        build += BCD[3]
    elif i == "4":
        build += BCD[4]
    elif i == "5":
        build += BCD[5]
    elif i == "6":
        build += BCD[6]
    elif i == "7":
        build += BCD[7]
    elif i == "8":
        build += BCD[8]
    elif i == "9":
        build += BCD[9]
    else:
        print("incorrect input")

print(build)

