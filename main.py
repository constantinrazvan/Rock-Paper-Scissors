import time
import os

from userOneClass import playerOne
from userTwoClass import playerTwo

print("Rock, Papper, Scissors Game")
time.sleep(3)
os.system("clear")

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
