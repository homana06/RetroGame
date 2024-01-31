#import pygame
from Character import *
from Maze import maze_array
print(maze_array)
pygame.init()
pygame.joystick.init()
try:
  pygame.mixer.init()
except pygame.error:
  print("error line 8")

frame = 0
Blue = (0, 0, 255)
Black = (0,0,0)
backx = 0
backy = 0
screen = pygame.display.set_mode([800, 800])
pygame.display.set_caption("The Adventures of Dolphin-San")
try:                                                  # Attempts to load the music, turned off for development, its loud
  pygame.mixer.music.load("Music/Brinstar.mp3")
  pygame.mixer.music.set_volume(-0.5)
  pygame.mixer.music.play(-1)
except pygame.error:
  print("Error loading or playing the music file.")
clock = pygame.time.Clock()
scalefactor = 2400


running = True
background1 = pygame.image.load("images/background.png")
background_size = (scalefactor,scalefactor)
backgroundf = pygame.transform.scale(background1,background_size)
player = Dolphin(200, 400, "images/DolphinLeft.png", "images/DolphinLeft2.png",
                 "images/DolphinRight.png", "images/DolphinRight2.png")
#---------------Joystick Movement--------------------------------------|||||||||||||||||||||||||||||||
keys = pygame.key.get_pressed()
num_joysticks = pygame.joystick.get_count()

if num_joysticks > 0:
  joystick = pygame.joystick.Joystick(0)
  print("initialised joystick1")
  if not joystick.get_init():
    print("Controller not connected")
  else:
    joystick.init()
    print("initialised joystick2")
else:
  joystick = None  # No joystick available
#-----------------------------------------------------Run Loop----------------------------------------------------------------------------------------------------------------------------------
while running:  #main running loop
  keys = pygame.key.get_pressed()
  screen.fill(Black)
  x = player.get_x()      # Background movement
  y = player.get_y()
  print(x,y)
  if x >= 705 and backx > -(scalefactor - 800):# - 800 keeps it completly within frame
    backx = backx - 5
  elif x <= 15 and backx < 0:
    backx = backx + 5

  if y >= 705 and backy > -(scalefactor - 800):
    backy = backy - 5
  elif y <= 15 and backy < 0:
    backy = backy + 5

  screen.blit(backgroundf, (backx, backy))
# loading the maze ------ Logic Errors here I presume
  start_row = max(0, int(backy / 30))  # Assuming each maze cell is 30 pixels
  end_row = min(len(maze_array), int((backy + 800) / 30))

  start_col = max(0, int(backx / 30))
  end_col = min(len(maze_array[0]), int((backx + 800) / 30))

  # Draw the visible portion of the maze
  for row in range(start_row, end_row):
    for col in range(start_col, end_col):
      cell_value = maze_array[row][col]
      wall = pygame.image.load("images/Testwall1.png")

      if cell_value == 1:  # Assuming 1 represents a wall
        wall_rect = wall.get_rect()
        wall_rect.topleft = (col - start_col) * 30, (row - start_row) * 30
        screen.blit(wall, wall_rect)
# as per usual 
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT:
      running = False

  if event.type == pygame.JOYAXISMOTION:
    if event.axis == 0 or event.axis == 1:
      player.move_joystick(joystick, frame, screen)


  if keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d] or keys[
      pygame.K_w]:  # Combine the if-elif branches using logical or operator
    player.move(keys, frame, screen)
    if frame > 0:
      frame -= 1
    else:
      frame += 1
  else:
    player.draw(screen)
  clock.tick(100)

  pygame.display.flip()
pygame.mixer.music.stop()
pygame.quit()
