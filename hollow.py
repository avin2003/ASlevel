
size = int(input("Input number of rows:"))
for row in range(1,(size+1)):
    for col in range(1,(2*size)):
        if row== size or row+col== size+1 or col-row== size-1:
            print("A",end = "")
        else:
            print(end=" ")
    print()


