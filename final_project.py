import pygame as py

WIDTH = 1024
HEIGHT = WIDTH / 16*9
player_info = None
player_size = 20

screen = py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption("TAG")

# COLORS
RED = (255,0,0)
BLUE = (0,0,255)
FREEZE_COLOR = (66, 167, 245)
YELLOW = (14,190,230)
WALL_COLOR = (77, 76, 76)

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
      self.rect.x -= self.p_vel
  def player_wall_up_y(self, player):
    if py.sprite.spritecollideany(player, wall_sprites):
      self.rect.y += self.p_vel
  def player_wall_left_x(self, player):
    if py.sprite.spritecollideany(player, wall_sprites):
      self.rect.x += self.p_vel
  def player_wall_down_y(self, player):
    if py.sprite.spritecollideany(player, wall_sprites):
      self.rect.y -= self.p_vel

  
  #DETECTS COLLISION WITH SLOW WALLS
  #right
  def player_slow_wall_right_x(self, player):
    if py.sprite.spritecollideany(player, slow_wall_sprites):
      self.rect.x -= 2
  #left
  def player_slow_wall_left_x(self, player):
    if py.sprite.spritecollideany(player, slow_wall_sprites):
      self.rect.x += 2  
  #up    
  def player_slow_wall_up_y(self, player):
    if py.sprite.spritecollideany(player, slow_wall_sprites):
      self.rect.y += 2
  #down
  def player_slow_wall_down_y(self, player):
    if py.sprite.spritecollideany(player, slow_wall_sprites):
      self.rect.y -= 2


  #TAGGED
  def tag(self, player):
    if py.sprite.spritecollideany(player, slow_wall_sprites):
      pass

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



# class SlowOrb:
#   def __init__(self, slow_x, slow_y):
#     self.slow_x = slow_x
#     self.slow_y = slow_y
#     self.slow_vel = 1
    
#   #CREATES THE SLOW ORBS 
#   def create_slows(self, screen):
#     py.draw.rect(screen, FREEZE_COLOR, self.slow_x, self.slow_y, 8,8)



# class InverOrb:
#   def __init__(self, invert_x, invert_y):
#     self.invert_x = invert_x
#     self.invert_y = invert_y
#     self.invert_vel = 2

#   # DRAWS INVERT ORBS 
#   def create_invert(self, screen):
#     py.display.rect(screen, YELLOW, (self.inver_x, self.invert_y, 5,5))



clock = py.time.Clock()
FPS = 60

all_sprites = py.sprite.Group()
all_sprites.add(player_1_sprite, player_2_sprite, wall_sprites, slow_wall_sprites)


running = True
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

    
  #DETECT PLAYER COLLISION
  if py.sprite.spritecollideany(player_1, player_2_sprite):
    if player_1.tagged == False:
      print("test")
  if py.sprite.spritecollideany(player_2, player_1_sprite):
    if player_2.tagged == False:
      pass
    
  #DRAWING THE WALLS
  wall_sprites.draw(screen)
  slow_wall_sprites.draw(screen)

  #DRAWING THE PLAYERS
  player_1_sprite.draw(screen)
  player_1.player_border_collision()

  player_2_sprite.draw(screen)
  player_2.player_border_collision()
  
  
py.quit()
quit()