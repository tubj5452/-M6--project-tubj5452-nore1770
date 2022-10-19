import random
import time
import datetime
from random import randint


yesNo = ["yes", "no"]
equations = {"x^3 = 8, what is x":"2", "What is the derivative of 1/x":"-1/(x^2)", "Simplify 76/8":"19/2", "Expand (x + 3)^2":"x^2+6x+9"}
options = ["restart", "quit"]
riddles = {"What has to be broken before you can use it?" : "egg" , "I am tall when I am young and short when I am old. What am I?" : "candle"}
sentences = ["I like bananas", "Programming is hard but fun!", "In my free-time i only study :("] #["a","b","c"]#["I like bananas", "Programming is hard but fun!", "In my free-time i only study :("]


sumPoints = 0
player = input("Your name: ")



def math(situation):
    print(f"\nTry to solve this question to {situation}\n\nYou have 3 guesses")
    equation = random.choice(list(equations))
    print(equation)
     
    points = 3
    while points <= 3:
        playerAnswer = checkAnswer(input("Answer: "))
        if playerAnswer == equations[equation]:
            print(f"Correct! You have earned {points} point(s)")
            equations.pop(equation)
            return points
        elif points == 1:
            points == 0
            return "gameOver"
        else:
            points -= 1
            print(f"Incorrect! You have {points} guess(es) left")

def askRiddle(situation):
    print(f"You have to solve this riddle to {situation}.\nGood luck!\n")
    riddle = random.choice(list(riddles))
    print(riddle)
    points = 3
        
    while points <= 3:
        playerAnswer = checkAnswer(input("Answer: "))

        if playerAnswer == riddles[riddle]:
            print(f"Correct! You have earned {points} point(s) and completed this {situation}")
            riddles.pop(riddle)
            return points
        elif points == 1:
            points == 0
            return "gameOver"
        else:
            points -= 1
            print(f"Incorrect! You have {points} guess(es) left")   
            
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
    while points <= 3:
        playerAnswer = checkAnswer(input("Answer: "))
        if playerAnswer == str(answer):
            print(f"Correct! You have earned {points} point(s) and managed to {situation}")
            return points
        elif points == 1:
            points == 0
            return "gameOver"
        else:
            points -= 1
            print(f"Incorrect! You have {points} guess(es) left")        
        
def binaryCodeAnswer(random):
    index = 4
    answer = 0
    for n in random:
        if n == '1':
            answer = answer + 2**(index)
        index -= 1
    return answer


def speedGame(situation):
    start(f"This is a speed-game. You need to write the sentence within 10 seconds to {situation}\nYou have 3 tries and the time restarts\n Are you ready?", yesNo)  
    sentence = random.choice(list(sentences))
    print(f"\nYour sentence is: {sentence}\n")
    sentence = checkAnswer(sentence)
    
    s = 5
    points = 3
    
    print("Your time starts in: ")
    while s >= 0:
 
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds = s)   
        # Prints the time left on the timer
        print(timer, end="\r")#----------------------------------------- EXPERIMENTERA MED
        # Delays the program one second
        time.sleep(1)
        # Reduces total time by one second
        s -= 1
        
    print("")  
    
    
    while True:
        t1 = time.time()
        playerAnswer = checkAnswer(input("Answer here: "))
        t2 = time.time()
        t = t2 - t1
    
        if t > 10:
            sumPoints = 0
            return "gameOverTime"
        elif playerAnswer == sentence:
            print(f"Correct! You have earned {points} point(s)")
            return points
        elif points == 1:
            return "gameOverIncorrect"
        else:
            points -= 1
            print(f"Incorrect! You have {points} guess(es) left")        
            
def menu(prompt, options, sumPoints):
    printList(f"{prompt}\nTotal points earned: {sumPoints}\n\nWhat do you want to do?\n", options)
    
    while True: 
        action = input(f"Action: ")
        if action == "quit":
            break
        elif action == "restart":
            return action
            
def start(prompt, strings):
    printList(f"{prompt}", yesNo)
    print()
        
    while True: 
        action = input(f"Choice: ")
        if action == "no" and are_you_sure(yesNo) == "no" or action == "yes": 
            return "playerIsReady"  
       
        
def are_you_sure(strings):
    printList("Are you sure?", yesNo)
        
    while True: 
        action = input(f"\nChoice: ")
        if action == "yes":
            print(f"\nHow unfortunate {player} :(, we hope you are ready next time!\nGoodbye!")
            quit()
        elif action == "no":
            print("\nGreat! Then let's continue")
            return action
    
def printList(prompt, strings):
    print(f"\n{prompt}")
    for n in strings:
        print (f"* {n}")
        
def checkAnswer(playerInput):
    step1 = playerInput.replace(" ", "")
    step2 = step1.lower()
    return(step2)
    


  
#Vissa gameOver vill vi bara ska restarta det specifika spelet, medan andra blir total gameOver. 
def main(sumPoints):
    
    if start(f"Welcome {player}! Are you ready for your adventure?", yesNo) == "playerIsReady":
        print("Introduction to story")
        print("You meet the kingdom's fairy to recieve directions, but its not for free...")

        while True:
            result = math("get the directions ")
            if result == "gameOver":
                print("You are out of guesses and you've annoyed the fairy slightly. She is kind enough to let you try again, but only if you can answer her riddle first.")
                result = askRiddle("get another chance")
                if result == "gameOver":
                    print("Oh no! This is your last chance. The fairy is getting angry at you stupidity. She could attack if you fail the next task.")
                    result = speedGame("survive")
                    if result == "gameOverTime" or result == "gameOverIncorrect":
                        menu(f"To slow!\nThe fairy is furious...\nGame over!\n", options, sumPoints)
                        return False
                    else:
                        True
                else:
                    True
            else:
                sumPoints = result
                print("Congratulations! You receved directions from the fairy")
                print(f"\nTotal points earned so far: {sumPoints}")
                break

    print("continue story(to the library)")
    while True:
        result = binaryCode("open the door and enter the library")
        if result == "gameOver":
            sumPoints = sumPoints - 1
            print("\nUnfortunately you failed to open the door and therefore you've lost 1 point.\n You get to try again.\n")
        else:
            sumPoints = sumPoints + result
            print(f"\nGood job, {player}! You opened the door to the library.")
            print(f"\nTotal points earned so far: {sumPoints}")
            break

    print("continue story(in the library)")
    result = speedGame("find the correct book before the angry librarian comes back")   
    if result == "gameOverTime":
        menu(f"You were too slow!\nThe angry librarian found you...\nGame over!\n", options, sumPoints)
        return False
    elif result == "gameOverIncorrect":
        menu(f"You didn't find the book in time and the angry librarian found you...\nGame over!\n", options, sumPoints)            
    else:
        sumPoints = sumPoints + result
        print(f"\nYou did it, {player}! You found the book in time!")
        print(f"\nTotal points earned so far: {sumPoints}")
    
    print("continue story(down in basement)")    
    
    while True:
        result = askRiddle("get an ingredient from the goblin")
        if result == "gameOver":
            print("*Gasp!* The goblin is upset that you don't know the riddles.")
            result = speedGame("survive")
            if result == "gameOverTime" or result == "gameOverIncorrect":
                menu(f"Oh no!\nThe goblin went to attack...\nGame over!\n", options, sumPoints)
                return False
            else:
                True      
    else:
        sumPoints = sumPoints + result
        print("Yaay! The goblin gave you the ingredient!")
        print(f"\nTotal points earned so far: {sumPoints}")
    
    print("continue story(to chest - you see a chest in the corner and the goblin alows you to open it if you get the right code. )")    
    result = binaryCode("open the chest")
    if result == "gameOver":
        menu(f"Incorrect!\nGame over!\n", options, sumPoints)
        return False
    else:
        sumPoints = sumPoints + result
        print("Congratulations! You managed to open the chest")
        print(f"\nTotal points earned so far: {sumPoints}")
    
    print("continue story(the fairy show up to give you more directions)")
    result = math("get the directions ")
    if result == "gameOver":
        menu(f"Incorrect!\nGame over!\n", options, sumPoints)
        return False
    else:
        sumPoints = result
        print("Congratulations! You receved directions from the fairy")
        print(f"\nTotal points earned so far: {sumPoints}")
        
    print("continue story(to the witch)")
    result = askRiddle("get help from the witch")       
    if result == "gameOver":
        menu(f"Incorrect!\nGame over!\n", options, sumPoints)
        return False
    else:
        sumPoints = sumPoints + result
        print("Congratulations! The witch found you worthy to help")
        print(f"\nTotal points earned so far: {sumPoints}")
    
    
    
  #  if start(f"Ready for the next game?", yesNo) == "playerIsReady":
         
        

  #  if start(f"Ready for the next game?", yesNo) == "playerIsReady":
   #     result = binaryCode("do something")
        
    
    
 #   if start(f"Ready for the next game?", yesNo) == "playerIsReady":
   #     result = speedGame("do something")   
         
        
while True: 
    if main(sumPoints) == False:
        sumPoints = 0
        main(sumPoints)