import time
import os

print("Rock, Papper, Scissors Game")
time.sleep(3)
os.system("clear")

#Player one
class playerOne:
    def __init__(self):
        self.username_playerOne = input('What is your name player one? \n')
        self.player_one_score = 0

      
#Player two
class playerTwo:
    def __init__(self):
        self.username_playerTwo = input('What is your name player two? \n')
        self.player_two_score = 0


#Init game
def start_game():
    print("Game started!")


first_player = playerOne()
second_player = playerTwo()
score = first_player.player_one_score + second_player.player_two_score

print(
    f"Welcome, {first_player.username_playerOne} and {second_player.username_playerTwo}!"
)
time.sleep(2)
os.system("clear")

players_input = input("Are you ready for the game? (y/n) \n")
os.system("clear")

if players_input == "y" or players_input == "Y":
    start_game()
else:
    os.system("clear")
