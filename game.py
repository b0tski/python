# 17 November 2022
import random
import time




class Game:
    def __init__(self, lives):
        self.score = 0
        self.initial_lives = lives
        self.lives = self.initial_lives
        self.clicks = 0
        self.roll = random.randint(1, 10)
        self.score_to_beat = 25
        print("Game initializing up...")


    
    def game_loop(self):
        while self.lives > 0:
        
            self.round_loop()
        print("GAME OVER!! TRY AGAIN!!")
        try_again_input = input("TYPE 't' to TRY AGAIN OR \nTYPE anything else to QUIT ").lower()
        if try_again_input == "t":
            self.lives = self.initial_lives
            self.game_loop()
        else: 
            return


    def round_loop(self):
        time.sleep(1)
        print("ROUND STARTED!")
        while self.clicks <= self.roll:
            time.sleep(1)
            user_input = input("(h) to CONTINUE/ ANYTHING ELSE to QUIT : ").lower()

            if user_input == "h":
                self.clicks += 1
            else:  # USER QUIT ROUND!!
                self.score += self.clicks
                self.clicks = 0
                self.roll = random.randint(1, 10)
                print(f"Your SCORE: {self.score}")
                time.sleep(1.5)
                return
        print("YOU LOST A LIFE!!") # USER LOST THE ROUND!!
        self.lives -= 1
        self.score += self.clicks
        self.clicks = 0
        self.roll = random.randint(1, 10)
        return

