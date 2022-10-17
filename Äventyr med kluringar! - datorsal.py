import random
import time
import datetime
from random import randint

yes_no = ["yes", "no"]
equations = {"x^3 = 8, what is x":"2", "What is the derivative of 1/x":"-1/(x^2)", "Simplify 76/8":"19/2", "Expand (x + 3)^2":"x^2+6x+9"}
options = ["restart", "quit"]
riddles = {"What has to be broken before you can use it?" : "egg" , "I am tall when I am young and short when I am old. What am I?" : "candle"}
sentences = ["I like bananas", "Programming is hard but fun!", "In my free-time i only study :("]


sum_points = 0

player = input("Your name: ")



def math(prompt, equations):
    print(f"\nTry to solve this question to complete this {prompt}\n\nYou have 3 guesses")
    equation = random.choice(list(equations))
    print(equation)
     
    points = 3
    while points <= 3:
        guess = input(f"\nAnswer: ")
        if guess == equations[equation]:
            print(f"Correct! You have earned {points} point(s)")
            return points
        elif points == 1:
            points == 0
            return menu(f"Incorrect!\nGame over!\n\nWhat do you want to do?\n", options, sum_points) 
        else:
            points -= 1
            print(f"Incorrect! You have {points} guess(es) left")

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
            
def binaryCode(prompt):
    print(f"You have to decode this binary code to {prompt}. \nGood luck!\n")
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
            
def menu(prompt, options, sum_points):
    print_list(f"{prompt}\nTotal points earned: {sum_points}\n", options)
    
    while True: 
        action = input(f"Action: ")
        if action == "quit":
            break
        elif action == "restart":
            sum_points = 0
            return start("Good luck, are you ready?", yes_no, sum_points)

            
def start(prompt, strings):
    print_list(f"{prompt}", yes_no)
    print()
        
    while True: 
        action = input(f"Choice: ")
        if action == "no" and are_you_sure(yes_no) == "no" or action == "yes": 
            return "player_is_ready"  #math("situation", equations, sum_points)
       
        
def are_you_sure(strings):
    print_list("Are you sure?", yes_no)
        
    while True: 
        action = input(f"\nChoice: ")
        if action == "yes":
            print(f"\nHow unfortunate {player} :(, we hope you are ready next time!\nGoodbye!")
            quit()
        elif action == "no":
            print("\nGreat! Then let's continue")
            return action
    
def print_list(prompt, strings):
    print(f"\n{prompt}")
    for n in strings:
        print (f"* {n}")

def speed_game(prompt, sentences, sum_points):
    start(f"{prompt}", yes_no, sum_points)
   
    sentence = random.choice(list(sentences))

    s = 10

    while s > 0:
 
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds = s)
        
        # Prints the time left on the timer
        print(timer, end="\r")
 
        # Delays the program one second
        time.sleep(1)
 
        # Reduces total time by one second
        s -= 1
        
        players_sentence = input(f"Your sentence is: {sentence}\n")

 
    print("Bzzzt! The countdown is at zero seconds!")
 

        
    
#if start(f"Welcome {player}! Are you ready for your adventure?", yes_no) == "player_is_ready": 
    sum_points = sum_points + math("situation", equations)

    #sum_points = math("situation", equations, sum_points)
    print(f"\nTotal points earned so far: {sum_points}")

#if start(f"Ready for the next game?", yes_no) == "player_is_ready":
    sum_points = sum_points + math("situation", equations)

    #sum_points = math("situation", equations, sum_points)
    print(f"\nTotal points earned so far: {sum_points}")

if start(f"Ready for the next game?", yes_no) == "player_is_ready":
    sum_points = sum_points + binaryCode("do something")
    print(f"\nTotal points earned so far: {sum_points}")


#if start(f"Ready for the next game?", yes_no, sum_points) == "player_is_ready":
 #   sum_points = speed_game("This is a speed-game, you have 10 seconds to write the sentence correct.\nAre you ready?\n", sentences, sum_points)
 #   print(f"\nTotal points earned so far: {sum_points}")
    

                
        