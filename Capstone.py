import random
Keywords = [("constant",["named", "value", "cannot","execution"], "a named value that cannot change during the execution of a program"),
            ("variable",["named", "value", "can","execution"], "a named value that can change during the execution of a program"),
            ("parameter",["variable", "procedure", "function","pass","value"], "a variable applied to a procedure or function that allows one to pass in a value for the procedure to use."),
            ("argument",["passed", "value", "procedure","function"], "the value passed to a procedure or function."),
            ("Count controlled loop",["specific", "integer", "FOR","TO","NEXT"], "FOR TO NEXT ENDFOR, the identifier assigned must relate to integer data type, runs for specific amount of times"),
            ("Pre Controlled loop",["WHILE", "TRUE", "DO","never","executed"], "WHILE TRUE DO ENDWHILE, can be never executed"),
            ("Post condition loop",["REPEAT", "UNTIL", "once","boolean"], "REPEAT UNTIL, must be executed at least once, the condition must relate to Boolean so UNTIL TRUE or FALSE"),
            ("Accepting State",["state", "system", "valid","input"], "A state the system reaches when the input string is valid"),
            ("normal test data",["accepted", "test", "data","program"], "test data that should be accepted by a program"),
            ("abnormal test data",["rejected", "test", "data","program"], "test data that should be rejected by a program"),
            ("extreme test data",["limit", "test", "data","program","accepted"], "test data that is on the limit of that accepted by a program"),
            ("boundary test data",["limit", "test", "data","program","accepted","outside","rejected"], "test data that is on the limit of that accepted by a program or data that is just outside the limit of what is rejected by a program"),
            ("White box testing",["testing", "program", "structure","logic","every","path"], "a method of testing a program that tests the structure and logic of every path through the program module"),
            ("black box testing",["method", "testing", "program","inputs","outputs"], "method of testing a program that tests a modules inputs and outputs"),
            ("stub testing",["dummy", "modules", "testing"], "use of dummy modules for testing purposes"),
            ("alpha testing",["completed", "program", "house","development","team"], "testing of a completed or nearly completed program in house by development team"),
            ]
score = 0
print("Welcome to a keyword quiz, you will get points if your answer contains a certain number of correct words.")
def GetKeyword():
    global word
    word = random.choice(Keywords)
    print("Give the definition of",word[0])
    answer = input()
    print("this is the actual definition:", word[2])
    return answer

for run in range(2):
    answer = GetKeyword()
    answer1= answer.split()
    counter =0
    for i in answer1:
        if i in word[1]:
            counter += 1
    if counter >= len(word[1]):
        print("Correct")
        score += 1
    Keywords.remove(word)


def OutputScore(score):
    print("this was your final score",score)
    name=input("input your name so your score can be saved")
    with open("Rankings.txt","a") as whole_file:
        whole_file.write((name+':' + str(score)+'points' + "\n"))

OutputScore(score)

