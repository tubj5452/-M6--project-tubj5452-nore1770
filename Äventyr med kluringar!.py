import random
yes_no = ["yes", "no"]
equations = {"x^3 = 8, what is x":"2", "What is the derivative of 1/x":"-1/(x^2)", "Simplify 76/8":"19/2"}
options = {"r":"Restart game", "q":"Quit"} 


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
            points == 0 #######
            menu(f"Incorrect!\n\nGame over!\n\nTotal points earned: ", options) #{sum_points}
            return points ######
        else:
            points -= 1
            print(f"Incorrect! You have {points} guess(es) left")
            
            
def menu(prompt, options):
    print (f"{prompt}\nWhat do you want to do?")
    for n in options:
        print (f"\t{n}) {options[n]}")
    print()
    
    enter = True
    while enter: 
        action = input(f"Action: ")
        if action == "q":
            break
        elif action == "r":
            start("Good luck, are you ready?", yes_no)
            
def start(prompt, strings):
    print(f"\n{prompt}")
    for n in yes_no:
        print (f"* {n}")
        
    while True: 
        action = input(f"\nChoice: ")
        if action == "no":
            are_you_sure(yes_no)
            break
        elif action == "yes":
            math("situation", equations)
            break
        
def are_you_sure(strings):
    print("\nAre you sure?")
    for n in yes_no:
        print (f"* {n}")
        
    while True: 
        action = input(f"\nChoice: ")
        if action == "yes":
            print(f"\nHow unfortunate {player} :(, we hope you are ready next time!\nGoodbye!")
            break
        elif action == "no":
            print("\nGreat! Then let's continue")
            math("situation", equations)
            break
            
start(f"Welcome {player}! Are you ready for your adventure?", yes_no)


        

        