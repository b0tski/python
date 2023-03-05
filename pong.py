

import pygame as py
import random
import time


py.mixer.init()
py.init()

clock = py.time.Clock()

WIDTH = 800
HEIGHT = WIDTH / 16*9
flags = py.SCALED | py.FULLSCREEN
screen = py.display.set_mode((WIDTH, HEIGHT), flags=flags, vsync=1)


# COLOR
GRAY = (60, 64, 77)
PLAYER_WHITE = (206, 209, 219)
DARK_GRAY = (152, 152, 158)

font = py.font.SysFont(None, 72)
title_font = py.font.SysFont("serif typeface", 90)

second_font = py.font.SysFont(None, 50)
next_font = py.font.SysFont("serif typeface", 70)
again_font = py.font.SysFont("serif typeface", 40)


py.display.set_caption("PONG")


# MUSIC
py.mixer.music.load("resources\\ball_sound.ogg")
py.mixer.music.set_volume(1)


# STARTING BUTTON
button_width = 130
button_height = 45
next_button = py.Rect(560, 400, button_width, button_height)


button_boolean = True

# PLAYER 1 PHYSICS
p1_x = 49
p1_y = 180

p1_width = 20
p1_height = 150
player_1 = py.Rect(p1_x, p1_y, p1_width, p1_height)
p1_vel = 3
p1_score = 0


# PLAYER 2 PHYSICS

p2_x = 735
p2_y = 180

p2_width = 20
p2_height = 150
player_2 = py.Rect(p2_x, p2_y, p2_width, p2_height)
p2_vel = 3
p2_score = 0


# MID LINE
midline = py.Rect(399, 0, 10, 500)

# BALL PYISICS

first_bounce = True
ball_x = WIDTH / 2
ball_y = HEIGHT / 2

ball_width = 20
ball_height = 20
ball = py.Rect(ball_x, ball_y, ball_width, ball_height)
ball_speed = [5, 0]

# TITLE BALL
title_ball = py.Rect(ball_x, ball_y, ball_width, ball_height)
title_ball_speed = [5, 4]

# Functions


def score_p1():

    text_score1 = font.render(str(p1_score), True, PLAYER_WHITE)
    screen.blit(text_score1, (325, 400))


def score_p2():
    text_score2 = font.render(str(p2_score), True, PLAYER_WHITE)
    screen.blit(text_score2, (450, 400))


def tip_off():

    ball[0] = ball_x
    ball[1] = ball_y
    ball_speed[1] = 0
    player_1[1] = p1_y
    player_2[1] = p2_y
    py.time.wait(500)


FPS = 100

# RUNS LOOPS
title_run = True
run = False
final_screen = False

while title_run:

    clock.tick(FPS)

    for event in py.event.get():

        if event.type == py.QUIT:
            title_run = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                title_run = False

    first_time = py.time.get_ticks()

    title_ball[0] += title_ball_speed[0]
    title_ball[1] += title_ball_speed[1]

    if title_ball[1] > HEIGHT - title_ball[3] or title_ball[1] < 0:
        title_ball_speed[1] *= -1

# RIGHT SIDE
    if title_ball[0] > WIDTH - title_ball[2]:
        title_ball_speed[0] *= -1

# LEFT SIDE
    if title_ball[0] < 0:
        title_ball_speed[0] *= -1

    # DRAWINGS
    py.draw.rect(screen, PLAYER_WHITE, ball)

    screen.fill(GRAY)
    py.draw.rect(screen, PLAYER_WHITE, midline)

    py.draw.rect(screen, PLAYER_WHITE, title_ball)

    title = font.render("P O N G", False, PLAYER_WHITE)
    screen.blit(title, (30, 35))

# NEXTT BUTTON
    py.draw.rect(screen, PLAYER_WHITE, next_button)
    next_text = second_font.render("NEXT", False, GRAY)
    screen.blit(next_text, (579, 405))

    mouse = py.mouse.get_pos()
    # print(mouse)

    if event.type == py.MOUSEBUTTONDOWN:
        if next_button[0] <= mouse[0] <= next_button[0] + next_button[2] and next_button[1] <= mouse[1] < next_button[1] + next_button[3]:
            title_run = False
            run = True

    py.display.update()

# AMOUNT OF TIME
timer = 5

# GAME SCREEN
while run:
    clock.tick(FPS)

    for event in py.event.get():

        if event.type == py.QUIT:
            run = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                run = False

    keys = py.key.get_pressed()

    screen.fill(GRAY)

    timer -= 1/FPS
    time = font.render(str(int(timer + 1)), False, PLAYER_WHITE)
    screen.blit(time, (10, 10))

    if timer <= 0:
        run = False
        final_screen = True

    # DEFAULT SPEED
    ball[0] += ball_speed[0]
    ball[1] += ball_speed[1]

    # PLAYER 1
    if keys[py.K_w] and player_1[1] > 0:
        player_1[1] -= p1_vel

    if keys[py.K_s] and player_1[1] < HEIGHT - p1_height:
        player_1[1] += p1_vel

    # PLAYER 2
    if keys[py.K_i] and player_2[1] > 0:
        player_2[1] -= p2_vel

    if keys[py.K_k] and player_2[1] < HEIGHT - p2_height:
        player_2[1] += p2_vel

    # Wall collision

    if ball[1] > HEIGHT - ball[3] or ball[1] < 0:
        ball_speed[1] *= -1
        py.mixer.music.play()
    # RIGHT SIDE
    if ball[0] > WIDTH - ball[2]:
        py.mixer.music.play()
        p1_score += 1
        first_bounce = True
        tip_off()

    # LEFT SIDE
    if ball[0] < 0:
        py.mixer.music.play()
        p2_score += 1
        first_bounce = True
        tip_off()

    rand_direction = random.randint(0, 1)

    # Ball collisioin
    if player_1.colliderect(ball):
        if first_bounce == True:
            first_bounce = False
            if rand_direction == 1:
                ball_speed[1] = -2
            if rand_direction == 0:
                ball_speed[1] = 2
        py.mixer.music.play()

        if rand_direction == 1:
            ball_speed[0] *= -1
            ball_speed[1] *= -1
        if rand_direction == 0:
            ball_speed[0] *= -1

    if player_2.colliderect(ball):
        if first_bounce == True:
            first_bounce = False
            if rand_direction == 1:
                ball_speed[1] = -2
            if rand_direction == 0:
                ball_speed[1] = 2
        py.mixer.music.play()

        if rand_direction == 1:
            ball_speed[0] *= -1
            ball_speed[1] *= -1
        if rand_direction == 0:
            ball_speed[0] *= -1

    score_p1()
    score_p2()

    # DRAWING
    py.draw.rect(screen, PLAYER_WHITE, player_1)
    py.draw.rect(screen, PLAYER_WHITE, player_2)
    py.draw.rect(screen, PLAYER_WHITE, midline)

    py.draw.rect(screen, PLAYER_WHITE, ball)

    py.display.update()


# DECORATIONS
big_square = py.Rect(50, 50, 700, 350)
underline = py.Rect(305, 120, 190, 12)
play_again_button = py.Rect(310, 340, 180, 35)


while final_screen:
    clock.tick(FPS)

    for event in py.event.get():

        if event.type == py.QUIT:
            final_screen = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                final_screen = False

    mouse = py.mouse.get_pos()

    # play again hitbot
    if event.type == py.MOUSEBUTTONDOWN:
        if play_again_button[0] <= mouse[0] <= play_again_button[0] + play_again_button[2] and play_again_button[1] <= mouse[1] < play_again_button[1] + play_again_button[3]:
            final_screen = False
            title_run = True

    screen.fill(DARK_GRAY)
    
    # Big Square
    py.draw.rect(screen, GRAY, big_square)

    # underline
    py.draw.rect(screen, PLAYER_WHITE, underline)

    # Title Winner
    title_winner = title_font.render("WINNER", False, PLAYER_WHITE)
    screen.blit(title_winner, (275, 60))

    # Winner
    if p1_score > p2_score:
        winner = next_font.render("PLAYER 1", False, PLAYER_WHITE)
        screen.blit(winner, (290, 200))
    elif p1_score < p2_score:
        winner = next_font.render("PLAYER 2", False, PLAYER_WHITE)
        screen.blit(winner, (290, 200))
    else:
        winner = next_font.render("TIE", False, PLAYER_WHITE)
        screen.blit(winner, (355, 200))

    # PLAY AGAIN BUTTON
    py.draw.rect(screen, PLAYER_WHITE, play_again_button)

    # PLAY AGAIN TEXT
    play_again = again_font.render("PLAY AGAIN", False, GRAY)
    screen.blit(play_again, (play_again_button[0] + 5, 345))

    py.display.update()

py.quit()

