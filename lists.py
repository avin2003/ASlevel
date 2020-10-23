itemnumber = [''] *10




oxo = [["#","#","#"],["#","#","#"],["#","#","#"]]

def print_oxo():
    print("    0    1    2")
    for i in range(3):
        print(i,oxo[i]) # The star prints without the []

def enter_oxo(ox):
    while True:
        y = int(input("row: "))
        x = int(input("column: "))
        if x>2 or y>2:
            print("Sorry oxo is not that big")
        elif  oxo[y][x] in ["X","O"]:
            print("Sorry, already taken")
        else:
            oxo[y][x] = ox
        break

print("Welcome to OXO!\n") # \n creates a new line.

while True:
    print_oxo()
    print("Player 1, your turn with X")
    enter_oxo("X")
    print_oxo()
    print("Player 2, your turn with O")
    enter_oxo("O")


