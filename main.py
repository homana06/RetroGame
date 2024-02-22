import pygame
import sys
from Maze import maze_array
from Character import *

def mazeload(screen, backx, backy, maze_array, background_width, background_height):
  # Calculate the size of each maze cell dynamically
  cell_width = background_width / len(maze_array[0])
  cell_height = background_height / len(maze_array)

  for row in range(len(maze_array)):
    for col in range(len(maze_array[0])):
      cell_value = maze_array[row][col]
      if cell_value == 1:  # Assuming 1 represents a wall
        wall = pygame.image.load("images/Testwall1.png")
        # Scale the wall image to fit the cell size
        wall = pygame.transform.scale(wall, (int(cell_width), int(cell_height)))
        wall_rect = wall.get_rect()
        # Calculate the position of the cell on the screen
        wall_rect.topleft = col * cell_width, row * cell_height
        screen.blit(wall, wall_rect)







print(maze_array)
pygame.init()
pygame.joystick.init()
try:
  pygame.mixer.init()
except pygame.error:
  print("error line 8")
run = pygame.image.load("images/Mater.jpg")

run = True
frame = 0
Blue = (0, 0, 255)
Black = (0,0,0)
backx = 0
backy = 0
screen = pygame.display.set_mode([800,600])
collide = pygame.Surface((800,800), pygame.SRCALPHA)
collide.fill((0, 0, 0, 0))
pygame.display.set_caption("The Adventures of Dolphin-San")
try:
  pygame.mixer.music.load("Music/Brinstar.mp3")
  pygame.mixer.music.set_volume(0)
  pygame.mixer.music.play(-1)
except pygame.error:
  print("Error loading or playing the music file.")
clock = pygame.time.Clock()
scalefactor = 800
background_width = 800
background_height = 600


running = True
background1 = pygame.image.load("images/background.png")
background_size = (scalefactor,scalefactor)
backgroundf = pygame.transform.scale(background1,background_size)
player = Dolphin(200, 400, "images/DolphinLeft.png", "images/DolphinLeft2.png",
                 "images/DolphinRight.png", "images/DolphinRight2.png")
#---------------movement--------------------------------------|||||||||||||||||||||||||||||||
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
  x = player.get_x()
  y = player.get_y()
  print(x,y)

  if x >= 710 and backx > -(scalefactor - 800):
    backx = backx - 5
  elif x <= 15 and backx < 0:
    backx = backx + 5

  if y >= 710 and backy > -(scalefactor - 800):
    backy = backy - 5
  elif y <= 15 and backy < 0:
    backy = backy + 5

  screen.blit(backgroundf, (backx, backy))

  mazeload(screen, backx, backy, maze_array, background_width, background_height)

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