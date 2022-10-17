import random
from random import randint

riddles = {"What has to be broken before you can use it?" : "egg" , "I am tall when I am young and short when I am old. What am I?" : "candle"}

def askRiddle(situation):
    print(f"You have to solve this riddle to {situation}.\nGood luck!\n")
    riddle = random.choice(list(riddles))
    print(riddle)
    points = 3
    while points > 0:
        playerAnswer = input("Answer: ")
        if playerAnswer == riddles[riddle]:
            print("Correct!")
            riddles.pop(riddle)
            return points
        else:
            points = points - 1
            if points > 0:
                print(f"\nThat is incorrect. You have {points} more guess(es).")
            else:
                print("\nThat is incorrect. You have no more tries.\nGame over.")
                return 0

#print(f"\nYou earned {askRiddle('do something')} points!")
                
yesOrNo = {"y" : "Say yes", "n" : "Say no"}

def viewAsList(alternatives):
    for alternative in alternatives:
        print(f"{alternative}) {alternatives[alternative]}")  
                
def makeAChoice(alternatives, choice, situation):
    print(f"You have to choose {choice} to {situation}.")
    viewAsList(alternatives)
    enter = True
    while enter:
        playerChoice = input("\nWhat do you want to do?\n")
        if playerChoice in alternatives:
            enter = False
            return playerChoice

    
#print(makeAChoice(yesOrNo, "to say yes or no", "do something"))
        

def binaryCode(situation):
    print(f"You have to decode this binary code to {situation}. \nGood luck!\n")
    enter = True
    index = 0
    random = ""
    points = 3
    while enter:
        random = (f"{random}{randint(0,1)}")
        index = index +1
        if index == 5:
            enter = False
    print(random)
    answer = binaryCodeAnswer(random)
    while points > 0:
        playerAnswer = input("\nAnswer: ")
        if playerAnswer == str(answer):
            print ("\nCorrect!")
            return points
        else:
            points = points - 1
            if points > 0:
                print(f"\nThat is incorrect. You have {points} more guess(es).")
            else:
                print("\nThat is incorrect. You have no more tries.\nGame over.")
                return 0
        
        
def binaryCodeAnswer(random):
    index = 4
    answer = 0
    for n in random:
        if n == '1':
            answer = answer + 2**(index)
        index = index - 1
    return answer
     
    
#binaryCode('do something')
    

def checkAnswer(playerInput):
    step1 = playerInput.replace(" ", "")
    step2 = step1.lower()
    return(step2)
    
    
playerInput = "Jag gillar pannkakor"
print(checkAnswer(playerInput))

    