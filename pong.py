# LUKE BOBROWSKI
# 2 DECEMBER 2023

import pygame as py


py.init()
clock = py.time.Clock()

WIDTH = 800
HEIGHT = 500
screen = py.display.set_mode((WIDTH,HEIGHT))


# COLOR
GRAY = (60, 64, 77)
PLAYER_WHITE = (206, 209, 219)
DARK_GRAY = (27, 31, 46)


py.display.set_caption("PONG")

# STARTING BUTTON
button_width = 50
button_height = 75


button_boolean = True 

#PLAYER 1 PHYSICS
p1_x = 50
p1_y = 180

p1_width = 20
p1_height = 150

p1_vel = 3

#PLAYER 2 PHYSICS

p2_x = 750
p2_y = 180

p2_width = 20
p2_height = 150

p2_vel = 3

#BALL PYISICS
ball_x = 385
ball_y = 250
ball_width = 12
ball_height = 12
ball_speed = 3




run = True

while run:

    clock.tick(60)

    for event in py.event.get():

        if event.type == py.QUIT:
            run = False

    keys = py.key.get_pressed()



    # STARTING SCREEN
    # while button_boolean == True:
    #     starting_button = py.draw.rect(screen, PLAYER_WHITE, (400, 250, button_width, button_height))
    #     if keys[py.CONTROLLER_BUTTON_LEFTSTICK] :
    #         pass
    
    #PLAYER 1
    if keys[py.K_w] and p1_y > 0:

        p1_y -= p1_vel

    if keys[py.K_s] and p1_y < 500 - p1_height:

        p1_y += p1_vel


    #PLAYER 2 
    if keys[py.K_i] and p2_y > 0:

        p2_y -= p2_vel


    if keys[py.K_k] and p2_y < 500 - p2_height:

        p2_y += p2_vel


    screen.fill(GRAY)

    

    player_1 = py.draw.rect(screen, PLAYER_WHITE, (p1_x, p1_y, p1_width, p1_height))
    player_2 = py.draw.rect(screen, PLAYER_WHITE, (p2_x, p2_y, p2_width, p2_height))

    ball = py.draw.rect(screen, PLAYER_WHITE, (ball_x, ball_y, 20, 20))




    py.display.update()


py.quit()
