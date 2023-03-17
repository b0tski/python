import pygame as py
import time 

py.init()

WIDTH = 1024
HEIGHT = WIDTH / 16*9
player_info = None
player_size = 20

#LOOPS 
running_info = True 
running = False
running_ending = False

screen = py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption("TAG")

#TYPES OF FONTS
clock_font = py.font.SysFont("serif typeface", 60)
info_font = py.font.SysFont("serif typeface", 40)
button_font = py.font.SysFont("serif typeface", 65)


# COLORS
WHITE = (206, 209, 219)
RED = (255,0,0)
BLUE = (0,0,255)
FREEZE_COLOR = (66, 167, 245)
YELLOW = (251, 248, 45 )
WALL_COLOR = (77, 76, 76)


class Object(py.sprite.Sprite):
  def __init__(self, RGB, button_x, button_y, button_width, button_height):
    """Creates a button to interact with"""
    
    py.sprite.Sprite.__init__(self)
    self.image = py.Surface([button_width, button_height])
    self.rect = self.image.get_rect()
    self.image.fill(RGB)
    self.rect.x = button_x
    self.rect.y = button_y


  def update_button(self):

    mouse_pos = py.mouse.get_pos()
    mouse_buttons = py.mouse.get_pressed()

    if self.rect.collidepoint(mouse_pos) and any(mouse_buttons):
      global running_info, running
      print("HI")
      running = True
      running_info = False     

      

object_sprites = py.sprite.Group()
button_sprites = py.sprite.Group()
all_title_sprites = py.sprite.Group()
button = Object(WHITE, 700,400,140,55)
line_1 = Object(WHITE, 120, 90, 250, 20)
info_player_1 = Object(RED, 75, 160, 20, 20)
info_player_2 = Object(BLUE, 75, 230, 20,20)
wall_info = Object(WALL_COLOR, 72, 300, 26, 50)
slow_wall_info = Object(FREEZE_COLOR, 72, 390, 26, 50)
divide_line = Object(WHITE, 505, 0, 25, HEIGHT)
tag_info = Object(YELLOW, 75, 500, 20, 20)
button_sprites.add(button)
object_sprites.add(line_1, info_player_1, info_player_2, wall_info, slow_wall_info, divide_line, tag_info)
all_title_sprites.add(button_sprites, object_sprites)


# WORDS
info_title = clock_font.render("INFO", False, WHITE)
player_1_text = info_font.render("- PLAYER 1", False, WHITE)
player_2_text = info_font.render("- PLAYER 2", False, WHITE)
wall_text = info_font.render("- WALL", False, WHITE)
slow_wall_text = info_font.render("- SLOWS PALYER DOWN", False, WHITE)
next_button_text = button_font.render("NEXT", False, (25,25,25))
tag_text = info_font.render("- TAGGED", False, WHITE)

#INFO SCREEN
running_info = True 

while running_info:
  for event in py.event.get():
    if event.type == py.QUIT:
      running_info = False

  all_title_sprites.update()
  button.update_button()
  py.display.update()
  screen.fill((25,25,25))

# DRAW OBJECTS 
  all_title_sprites.draw(screen)

  #DRAW WORDS 
  screen.blit(info_title, (200,40))
  screen.blit(player_1_text, (110, 157))
  screen.blit(player_2_text, (110, 227))
  screen.blit(wall_text, (110, 312))
  screen.blit(slow_wall_text, (110, 400))
  screen.blit(next_button_text, (710, 409))
  screen.blit(tag_text, (110, 498))



  

class Player(py.sprite.Sprite):
  
  def __init__(self, player_x, player_y, RGB):
    
    py.sprite.Sprite.__init__(self)
    self.image = py.Surface([player_size, player_size])
    self.rect = self.image.get_rect()
    self.image.fill(RGB)
    self.rect.x = player_x
    self.rect.y = player_y
    self.p_vel = 3
    self.tagged = False


   
#CONTROLS
  def move_up(self):
    self.rect.y -= self.p_vel
    
  def move_down(self):
    self.rect.y += self.p_vel
    
  def move_left(self):
    self.rect.x -= self.p_vel
    
  def move_right(self):
    self.rect.x += self.p_vel
  
  
  # DETECTS THE PLAYER COLLISION WITH THE BORDER
  def player_border_collision(self):
    if self.rect.x < 0:
        self.rect.x = 0
    if self.rect.x > WIDTH - player_size - 1:
        self.rect.x = WIDTH - player_size -1
    if self.rect.y < 0:
        self.rect.y = 0
    if self.rect.y > HEIGHT - player_size - 1:
        self.rect.y = HEIGHT - player_size - 1

  # DETECTS COLLISION WITH THE WALLS
  def player_wall_right_x(self, player):
    if py.sprite.spritecollideany(player, wall_sprites):
      self.rect.x -= self.p_vel +1
  def player_wall_up_y(self, player):
    if py.sprite.spritecollideany(player, wall_sprites):
      self.rect.y += self.p_vel +1
  def player_wall_left_x(self, player):
    if py.sprite.spritecollideany(player, wall_sprites):
      self.rect.x += self.p_vel +1
  def player_wall_down_y(self, player):
    if py.sprite.spritecollideany(player, wall_sprites):
      self.rect.y -= self.p_vel +1

  
  #DETECTS COLLISION WITH SLOW WALLS
  #right
  def player_slow_wall_right_x(self, player):
    if py.sprite.spritecollideany(player, slow_wall_sprites):
      self.rect.x -= self.p_vel -1
  #left
  def player_slow_wall_left_x(self, player):
    if py.sprite.spritecollideany(player, slow_wall_sprites):
      self.rect.x += self.p_vel -1
  #up    
  def player_slow_wall_up_y(self, player):
    if py.sprite.spritecollideany(player, slow_wall_sprites):
      self.rect.y += self.p_vel -1
  #down
  def player_slow_wall_down_y(self, player):
    if py.sprite.spritecollideany(player, slow_wall_sprites):
      self.rect.y -= self.p_vel -1

  
      
  #TAGGED
  def tag(self, player, color):
    # self.tagged = True
    # player.tagged = False
    self.p_vel = 4
    self.image.fill(YELLOW)
    player.p_vel = 3
    player.image.fill(color)


  #INVINCIBLE FRAMES 
    
  def timer(self, time_ticks, player):
    print("test")
    if time_ticks - py.time.get_ticks() > 5000:
      self.tagged = False
      player.tagged = True
      print("TEST")
    

    




#CREATES THE PLAYERS AND ADDS THEM TO PLAYER SPRITE GROUP
player_1_sprite = py.sprite.Group()
player_1 = Player(420,288,RED)
player_1_sprite.add(player_1)

player_2_sprite = py.sprite.Group()
player_2 = Player(584, 288, BLUE)
player_2_sprite.add(player_2)

player_sprites = py.sprite.Group()
player_sprites.add(player_1_sprite, player_2_sprite)



class Wall(py.sprite.Sprite):
  def __init__(self, wall_x, wall_y, wall_width, wall_height, RGB):

    py.sprite.Sprite.__init__(self)

    self.image = py.Surface([wall_width, wall_height])
    self.rect = self.image.get_rect()
    self.image.fill(RGB)
    self.rect.x = wall_x
    self.rect.y = wall_y


  #CREATE WALLS AND ADDS THEM TO WALL SPRITE GROUP
wall_sprites = py.sprite.Group()
wall_1 = Wall(75, 50, 25, 213, WALL_COLOR)
wall_2 = Wall(75, 328, 25, 258, WALL_COLOR)
wall_3 = Wall(175, 217, 145, 25, WALL_COLOR)
wall_4 = Wall(180, 364, 135,135, WALL_COLOR)
wall_5 = Wall(370, 263, 20, 70, WALL_COLOR)
wall_6 = Wall(406, 413, 212, 25, WALL_COLOR)
wall_7 = Wall(468, 175, 88, 25, WALL_COLOR)
wall_8 = Wall(634, 263, 20, 70, WALL_COLOR)
wall_9 = Wall(709, 364, 135, 135, WALL_COLOR)
wall_10 = Wall(704, 217, 145,25, WALL_COLOR)
wall_11 = Wall(924,50, 25, 213, WALL_COLOR)
wall_12 = Wall(924, 328, 25, 258, WALL_COLOR)
wall_13 = Wall(95, 105, 829, 25, WALL_COLOR)
wall_14 = Wall(452, 0, 120,50, WALL_COLOR)
wall_sprites.add(wall_1, wall_2, wall_3, wall_4, wall_5, wall_6, wall_7, wall_8, wall_9, wall_10, wall_11, wall_12, wall_13, wall_14)


  #CREATE WALLS AND ADDS THEM TO SLOW WALL SPRITE GROUP
slow_wall_sprites = py.sprite.Group()
slow_wall_1 = Wall(499, 50, 25, 55, FREEZE_COLOR)
slow_wall_2 = Wall(237, 155, 25, 37, FREEZE_COLOR)
slow_wall_3 = Wall(767 ,155, 25, 37, FREEZE_COLOR)
slow_wall_4 = Wall(100, 400, 80, 25, FREEZE_COLOR)
slow_wall_5 = Wall(844, 400, 80, 25, FREEZE_COLOR)
slow_wall_sprites.add(slow_wall_1, slow_wall_2, slow_wall_3, slow_wall_4, slow_wall_5)



clock = py.time.Clock()
FPS = 60

all_sprites = py.sprite.Group()
all_sprites.add(player_1_sprite, player_2_sprite, wall_sprites, slow_wall_sprites)

player_1.tagged = True
player_1.p_vel = 4
player_1.image.fill(YELLOW)

# AMOUNT OF TIME ON THE CLOCK
timer = 60


while running:
  for event in py.event.get():
    if event.type == py.QUIT:
      running = False

  click = py.mouse.get_pos()
  if event.type == py.MOUSEBUTTONDOWN:
    print(click)

#FPS
  clock.tick(FPS)
  py.display.update()
  all_sprites.update()

#BACKROUND
  screen.fill((25,25,25))

  #CLOCK
  timer -= 1/FPS
  game_clock = clock_font.render(str(int(timer + 1)), False, WHITE)
  if timer < 0: 
    running = False
    running_ending = True 


# PLAYER CONTROLS 
  keys = py.key.get_pressed()
  if keys[py.K_w]:
    player_1.move_up()
    player_1.player_wall_up_y(player_1)
    player_1.player_slow_wall_up_y(player_1)
  if keys[py.K_s]:
    player_1.move_down()
    player_1.player_wall_down_y(player_1)
    player_1.player_slow_wall_down_y(player_1)
  if keys[py.K_a]:
    player_1.move_left()
    player_1.player_wall_left_x(player_1)
    player_1.player_slow_wall_left_x(player_1)
  if keys[py.K_d]:
    player_1.move_right()
    player_1.player_wall_right_x(player_1)
    player_1.player_slow_wall_right_x(player_1)
    
  if keys[py.K_i]:
    player_2.move_up()
    player_2.player_wall_up_y(player_2)
    player_2.player_slow_wall_up_y(player_2)
  if keys[py.K_k]:
    player_2.move_down()
    player_2.player_wall_down_y(player_2)
    player_2.player_slow_wall_down_y(player_2)
  if keys[py.K_j]:
    player_2.move_left()
    player_2.player_wall_left_x(player_2)
    player_2.player_slow_wall_left_x(player_2)
  if keys[py.K_l]:
    player_2.move_right()
    player_2.player_wall_right_x(player_2)
    player_2.player_slow_wall_right_x(player_2)

    # COOLDOWN CLOCK
  # run_collision = True

  if py.sprite.spritecollideany(player_1, player_2_sprite):
    if player_1.tagged == True:
      player_2.tag(player_1, RED)
      collision_time = py.time.get_ticks()
      print(collision_time)
      player_1.timer(collision_time, player_2)
        


      # if player_2.tagged == True:
      #   player_1.tag(player_2, BLUE)
      #   collision_time = py.time.get_ticks()
      #   print(collision_time)
      #   player_2.timer(collision_time, player_1)



  

      
    
  #DRAWING THE WALLS
  wall_sprites.draw(screen)
  slow_wall_sprites.draw(screen)

  #DRAWING THE PLAYERS
  player_1_sprite.draw(screen)
  player_1.player_border_collision()

  player_2_sprite.draw(screen)
  player_2.player_border_collision()


  # DRAWS THE CLOCK
  if timer < 9:
    screen.blit(game_clock, (500, 7))   
  else: 
    screen.blit(game_clock, (488, 7))




while running_ending:
  for event in py.event.get():
    if event.type == py.QUIT:
      running_ending = False

  clock.ticks(FPS)
  py.display.update()

  
      
py.quit()
quit()
