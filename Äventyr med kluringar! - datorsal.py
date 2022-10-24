import random
import time
import datetime
from random import randint


yesNo = ["yes", "no"]
equations = {"x^3 = 8, what is x":"2", "What is the derivative of 1/x":"-1/(x^2)", "Simplify 76/8":"19/2", "Expand (x + 3)^2":"x^2+6x+9", "What is π/4 in degrees?":"45", "What is i^2?":"-1", "Calculate |−4|?":"4", "Solve for x: 3x = 1/2":"1/6"}
options = ["restart", "quit"]
riddles = {"What has to be broken before you can use it?" : "egg" , "I am tall when I am young and short when I am old. What am I?" : "candle", "The poor have me; the rich need me. Eat me and you will die. What am I?" : "nothing" , " They come at night without being called and are lost in the day without being stolen. What are they?" : "stars"}
sentences = ["I like bananas", "Programming is hard but fun!", "In my free-time I only study :(", "I hate to ride my sister's bike", "Lasagna is overrated", "Why do dragons not exist?"]


sumPoints = 0
player = input("Your name: ")



def math(situation):
    print(f"\nTry to solve this question to {situation}\nYou have 3 guesses\n")
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
            print(f"Correct! You have earned {points} point(s)")
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
            print(f"Correct! You have earned {points} point(s)")
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
    


  
def main(sumPoints):
    
    if start(f"Welcome {player}! Are you ready for your adventure?", yesNo) == "playerIsReady":
        print(f"\nIt's a beautiful spring morning in the kingdom. The sun is shining in through the window and you can hear birds singing ouside the castle walls. But you were awoken by worried voices outside of your door. Suddenly one of the guards rush in.\n\n'{player}! Come quick! Something terrible has happened to the king.'\n\nYou follow the guard to the king's room and you're met by a sad sight. The king is laying sick is his bed. He must have been poisoned.\n\n'I will find a cure and bring it to the king!' you say and storm out of the room to begin your mission. \n\nFirst you need to go to the library to find the recipe for the cure. But the castle is huge and you don't know how to get there. You decide to ask for help.\n")
        print("You meet the kingdom's fairy to receive directions, but it's not going to be free...")

        while True:
            result = math("get directions to the library")
            if result == "gameOver":
                print("You are out of guesses and you've annoyed the fairy. She is kind enough to let you try again, but only if you can answer her riddle first.")
                result = askRiddle("get another chance")
                if result == "gameOver":
                    print("Oh no! This is your last chance. The fairy is getting angry at your stupidity. She could attack if you fail the next task.")
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
                print(f"Total points earned so far: {sumPoints}")
                print("\nCongratulations! You received directions from the fairy.")
                break

    print(".\n.\n.\nYou make your way through the castle and end up at the door to the library. But it's locked...\n")
    while True:
        result = binaryCode("open the door and enter the library")
        if result == "gameOver":
            sumPoints = sumPoints - 1
            print("\nUnfortunately you failed to open the door and therefore you've lost 1 point.\n You get to try again.\n")
        elif result == "gameOver" and sumPoints == 0:
            menu(f"You are out of points...\nGame over!\n", options, sumPoints)
            break    
        else:
            sumPoints = sumPoints + result
            print(f"Total points earned so far: {sumPoints}")
            print(f"\nGood job, {player}! You opened the door to the library.")
            break

    print(".\n.\n.\nInside of the library it's dark, and just like everything else in the castle, it's very big. Usually the library is guarded by an angry librarian, but she seems to be gone at the minute...")
    result = speedGame("find the correct book before the angry librarian comes back")   
    if result == "gameOverTime":
        menu(f"You were too slow!\nThe angry librarian came back and found you...\nGame over!\n", options, sumPoints)
        return False
    elif result == "gameOverIncorrect":
        menu(f"You didn't find the book in time and the angry librarian found you...\nGame over!\n", options, sumPoints)            
    else:
        sumPoints = sumPoints + result
        print(f"Total points earned so far: {sumPoints}")
        print(f"\nYou did it, {player}! You found the book in time!")
    
    print(".\n.\n.\nYou quickly grab the book off of the shelf and sneak out of the library. You sit down outside the door to look through the book. As you're sitting down, you see the librarian approaching at the end of the corridor and quickly hide the book in your coat.\nWhew! That was really close!\nWhen the librarian once again is out of sight you open the book and read the recipe. You need a mystery liquid, special herbs and magical bugs. You think that the castle goblin probably has some bugs, so you make your way down into the dungeon...\n\nIn the dungeon you meet the goblin and ask him for help. He is willing to help, but not for free...\n")    
    
    while True:
        result = askRiddle("get the magical bugs from the goblin")
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
            print(f"Total points earned so far: {sumPoints}")
            print("\nYaay! The goblin gave you the magic bugs!")
            break

    print(".\n.\n.\nThe goblin points at the chest in the dark corner: 'Another necessary ingredient is in here'.")
    print("The chest is locked and you get a bit more nervous.\nThey allow you to open it, only if you get the right code... \n" )  
    while True:
        result = binaryCode("open the chest")
        if result == "gameOver":
            sumPoints = sumPoints - 1
            print("\nUnfortunately you failed to open the chest and therefore you've lost 1 point.\n You get to try again.\n")   
        elif result == "gameOver" and sumPoints == 0:
            menu(f"You are out of points...\nGame over!\n", options, sumPoints)
            break
        else:
            sumPoints = sumPoints + result
            print(f"Total points earned so far: {sumPoints}")
            print("\nCongratulations! You managed to open the chest and find a vial of a mysterious liquid")           
            break   
   

    print(".\n.\n.\nThe fairy pops into the goblins den and explain that the liquid is crucial for the cure and the witch may know how to mix it together")
    print("They offer guidande for the way, but not for free of course...")

    while True:
        result = math("get the directions to the witch")
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
            sumPoints = sumPoints + result
            print(f"Total points earned so far: {sumPoints}")
            print("\nCongratulations! The fairy was impressed and gives you directions for you to be on your way to the witch")
            print("Before you can exit the room the fairy says: 'Take these herbes, they may help' ")        
            break    
    
    
    print(".\n.\n.\nAfter tunneling the king's endless castle you arrive safely to the witch who can make the cure for the poisoned king with your ingredients\n")
    while True:
        result = askRiddle("get help from the witch")       
        if result == "gameOver":
            print("*Gasp!* The cure is not forming correctly, it needs to be stirred.")
            result = speedGame("stir or the cure will be a faliure")
        if result == "gameOverTime" or result == "gameOverIncorrect":
            menu(f"Oh no!\nThe making of the cure failed and the king will die...\nGame over!\n", options, sumPoints)
            return False
        else:
            sumPoints = sumPoints + result
            print(f"Total points earned so far: {sumPoints}")
            print("\nCongratulations! The cure was cultivated perfectly")
            break
        


    print(".\n.\n.\nYou watch the finished galaxy-like looking potion and thank the witch and prepare for your run back")
    print("Time is not on your side because the witch senses the king's condition worsen, you need to hurry!")
    
    result = speedGame("get the cure to the king in time")       
    if result == "gameOverTime" or result == "gameOverIncorrect":
            menu(f"The king died beacuse you were to slow.\nGame over!\n", options, sumPoints)
            return False
    else:
        sumPoints = sumPoints + result
        print(f"\nTotal points earned: {sumPoints}")
        print("Congratulations!\nYou arrived to the king in time and you were able to give him the cure.\nHis life as well as the kingdom was saved thanks to your efforts!!!")        
        if start(f"Game cleared!\nWhat do you want to do?", yesNo) == "playerIsReady":
            return False
        
        
        
while True: 
    if main(sumPoints) == False:
        sumPoints = 0
        main(sumPoints)
                
        
    

                
        
        
                
        
