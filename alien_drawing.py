# Luke Bobrowski
# 26 January 2023

import pygame as py
import random

py.init()

# SCREEN DIMENTIONS 
WIDTH  = 600
HEIGHT = 800

screen = py.display.set_mode((WIDTH, HEIGHT))

# STAR DIMENTIONS
star_size = 2
amount_starts = 1


class Stars:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
        self.width = star_size
        self.height = star_size

    def display_block(self, x, y):
        py.draw.ellipse(screen, (self.red, self.green, self.blue), ((x, y, self.width, self.height)))

W = Stars(255,255,255)
star_list = []

clock = py.time.Clock()
FPS = 60

running = True 

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    for count in range(1):
        ran_star_x = random.randint(1, 600)
        ran_star_y = random.randint(1, 800)
        W.display_block(ran_star_x, ran_star_y)
    

    clock.tick(FPS)
    py.display.update()

py.quit 