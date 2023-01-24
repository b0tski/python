

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

font = py.font.SysFont(None, 72)


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
player_1 = py.Rect(p1_x, p1_y, p1_width, p1_height)
p1_vel = 3
p1_score = 0

#PLAYER 2 PHYSICS

p2_x = 735
p2_y = 180

p2_width = 20
p2_height = 150
player_2 = py.Rect(p2_x, p2_y, p2_width, p2_height)
p2_vel = 3
p2_score = 0

#BALL PYISICS

ball_x = 385
ball_y = 250
ball_width = 20
ball_height = 20
ball = py.Rect(ball_x, ball_y, ball_width, ball_height)
ball_speed = [5,1]

# Functions 

def score_p1():

    text_score1 = font.render(str(p1_score), True, (0,0,0))
    screen.blit(text_score1, (435, 450))


def score_p2():
    text_score2 = font.render(str(p2_score), True, (0, 0, 0))
    screen.blit(text_score2, (400, 450))

run = True

while run:

    clock.tick(60)

    for event in py.event.get():

        if event.type == py.QUIT:
            run = False

    keys = py.key.get_pressed()

    screen.fill(GRAY)

    # STARTING SCREEN
    # while button_boolean == True:
    #     starting_button = py.draw.rect(screen, PLAYER_WHITE, (400, 250, button_width, button_height))
    #     if keys[py.CONTROLLER_BUTTON_LEFTSTICK] :
    #         pass

    # DEFAULT SPEED
    ball[0] += ball_speed[0]
    ball[1] += ball_speed[1]

    
    #PLAYER 1
    if keys[py.K_w] and player_1[1] > 0:
        player_1[1] -= p1_vel

    if keys[py.K_s] and player_1[1] < HEIGHT - p1_height:
        player_1[1] += p1_vel


    #PLAYER 2 
    if keys[py.K_i] and player_2[1] > 0:
       player_2[1] -= p2_vel


    if keys[py.K_k] and player_2[1] < HEIGHT - p2_height:
       player_2[1] += p2_vel


    # Wall collision

    
    if ball[1] > HEIGHT - ball[3] or ball[1] < 0:
        ball_speed[1] *= -1

    # RIGHT SIDE
    if ball[0] > WIDTH - ball[2]:
        ball_speed[0] *= -1
        score_p1()

    #LEFT SIDE
    if ball[0] < 0:
        ball_speed[0] *= -1
        score_p2()


    # Ball collisioin 
    if player_1.colliderect(ball):
        ball_speed[0] *= -1
    
    if player_2.colliderect(ball):
        ball_speed[0] *= -1



    
    # DRAWING
    py.draw.rect(screen, PLAYER_WHITE, player_1)
    py.draw.rect(screen, PLAYER_WHITE, player_2)

    py.draw.rect(screen, PLAYER_WHITE, ball)




    py.display.update()


py.quit()

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
