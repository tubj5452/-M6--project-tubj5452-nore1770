import random
yes_no = ["yes", "no"]
equations = {"x^3 = 8, what is x":"2", "What is the derivative of 1/x":"-1/(x^2)", "Simplify 76/8":"19/2", "Expand (x + 3)^2":"x^2+6x+9"}
menu = ["restart", "quit"]

sum_points = 0

player = input("Your name: ")



def math(prompt, equations, sum_points):
    print(f"\nTry to solve this question to complete this {prompt}\n\nYou have 3 guesses")
    equation = random.choice(list(equations))
    print(equation)
     
    points = 3
    while points <= 3:
        guess = input(f"\nAnswer: ")
        if guess == equations[equation]:
            print(f"Correct! You have earned {points} point(s)")
            return sum_points + points
        elif points == 1:
            points == 0
            return menu(f"Incorrect!\n\nGame over!\n\nTotal points earned: {sum_points}", menu, sum_points) 
          #  return sum_points + points
        else:
            points -= 1
            print(f"Incorrect! You have {points} guess(es) left")
            
            
def menu(prompt, menu, sum_points):
    print_list(f"{prompt}", menu)

 #   print (f"{prompt}\nWhat do you want to do?")
#    for n in options:
 #       print (f"\t{n}) {options[n]}")
 #  print()
    
    enter = True
    while enter: 
        action = input(f"Action: ")
        if action == "q":
            break
        elif action == "r":
            sum_points = 0
            return start("Good luck, are you ready?", yes_no, sum_points)
            #break
            #sum_points = sum_points + math("situation", equations)
            #return sum_points
       ##     return sum_points + math("situation", equations, sum_points)
           

            
def start(prompt, strings, sum_points):
   # print(f"\n{prompt}")
    print_list(f"{prompt}", yes_no)
    #for n in yes_no:
    #    print (f"* {n}")
        
    while True: 
        action = input(f"\nChoice: ")
        if action == "no" and are_you_sure(yes_no) == "no" or action == "yes": 
            #sum_points = sum_points + math("situation", equations)
            #return sum_points
            return math("situation", equations, sum_points)
 #       else:
  #          break
       
        
def are_you_sure(strings):
 #   print("\nAre you sure?")
    print_list("Are you sure?", yes_no)

  #  for n in yes_no:
   #     print (f"* {n}")
        
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

#def speed_game():
    

sum_points = start(f"Welcome {player}! Are you ready for your adventure?", yes_no, sum_points)
print(f"\nTotal points earned so far: {sum_points}")

sum_points = start(f"Ready for the next game?", yes_no, sum_points)
print(f"\nTotal points earned so far: {sum_points}")

#sumpoints = sumpoints + points
        

        