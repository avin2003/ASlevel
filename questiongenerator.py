
import random

command_words= ["Analyse","Assess","Calculate","Comment","Compare","Complete","Consider","Contrast","Define","Demonstrate","Describe","Develop","Draw","Discuss","Evaluate","Examine","Explain","Give","Identify","Justify","Outline","Predict","Sketch","State"]
meme_words=["Abstraction","Decomposition","Structured English","StepwiseRefinement","Flowcharts","Sequences","Loops","Selections"]

question= input("start? y/n")
while True:
    if question=="y":
        print(random.choice(command_words),random.choice(meme_words))
        question =input("next? y/n")
    else:
        break



