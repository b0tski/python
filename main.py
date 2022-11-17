# 17 Novmeber 2022
# Luke Bobrowski

import game
from game import Game
import random
import time 

def rest(duration):
    time.sleep(duration)
    print()





# Beginning

print("Welcome to bot's first game!\n He's a little rusty...")
rest(1)
print("This game is kinda like blackjack!")
rest(2)
print("You will start at 0 and every time you type in (h) it will go up one")
rest(3)
print("You can go up as much as you want!")
rest(2)
print("BUTTTT at some point, you will go over my number which means GAME OVER!!")
rest(3)
print("You got 3 tries to beat my HIGH SCORE of 25!!")
rest(2)
print("Good luck!")
rest(1)

user_lives = int(input("How many lives do u want? "))

bots_try = Game(user_lives)
bots_try.game_loop()

