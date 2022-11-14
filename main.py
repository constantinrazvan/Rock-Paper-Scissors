import time
import os

os.system("clear")
print("Rock, Paper, Scissors - The Game")
time.sleep(3) 
os.system("clear")

username_playerOne = input(str("What is your name Player One? \n"))
os.system("clear")

username_playerTwo = input(str("What is your name Player Two? \n"))
os.system("clear")

############################## 
def startGame(): 
    print("Game started!")
    
    score_playerOne = 0
    score_playerTwo = 0 
    
    playerOne_choice = input("Choose one: \n 1. Rock \n 2. Papper \n 3. Scissors \n")
    os.system("clear")

    playerTwo_choice = input("Choose one: \n 1. Rock \n 2. Papper \n 3. Scissors \n")
    os.system("clear")
    
    if playerOne_choice == "1" and playerTwo_choice == "2": 
        print("Congrats! Player Two won!")
        score_playerTwo += 1
        print(f"score is: {score_playerOne} | {score_playerTwo}")
    elif playerOne_choice == "2" and playerTwo_choice == "3": 
        print("Congrats! Player Two won!")
        score_playerTwo += 1
        print(f"score is: {score_playerOne} | {score_playerTwo}")
    elif playerOne_choice == "1" and playerTwo_choice == "3": 
        print("Congrats! Player one won!")
        score_playerOne += 1 
        print(f"score is: {score_playerOne} | {score_playerTwo}")
    elif playerOne_choice == "1" and playerTwo_choice == "1": 
        print("Tie")
        print(f"score is: {score_playerOne} | {score_playerTwo}")
    elif playerOne_choice == "2" and playerTwo_choice == "2": 
        print("Tie")
        print(f"score is: {score_playerOne} | {score_playerTwo}")
    elif playerOne_choice == "3" and playerTwo_choice == "3": 
        print("Tie")
        print(f"score is: {score_playerOne} | {score_playerTwo}")
    else: 
        print("Undefined")
        
# score_game = print(f"{score_playerOne} | {score_playerTwo}")

print(f"Welcome {username_playerOne} and {username_playerTwo}!")
os.system("clear")

users_choice = input(str("Are you ready for the game? (y/n) \n"))
os.system("clear")

if users_choice == "y": 
    startGame()
else: 
    raise ValueError(f"Your choice is invalid! -> {users_choice}") 




