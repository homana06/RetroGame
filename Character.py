import pygame
from Maze import *
screen = (800, 800)


class Dolphin():

  def __init__(self, x, y, image1, image2, image3, image4):
    self.x = x
    self.y = y
    self.walkl = [pygame.image.load(image1), pygame.image.load(image2)]
    self.walkr = [pygame.image.load(image3), pygame.image.load(image4)]
    self.rect = pygame.Rect(200, 400, 50, 50)
    self.rect.center = (x, y)
    self.vel = 5
    self.last = ["a"]

  def draw(self, surface):
    #pygame.draw.rect(surface, (0,0,255), self.rect)
    if self.last == "a":
      surface.blit(self.walkl[0], (self.x, self.y))
    else:
      surface.blit(self.walkr[0], (self.x, self.y))

  def move(self, keys, frame, surface):
    if keys[pygame.K_a]:  # Check if the "a" key is pressed
      if self.x - self.vel > 0:
        self.x -= self.vel
      self.last = "a"
    if keys[pygame.K_d]:  # Check if the "d" key is pressed
      if self.x + self.vel < 725:
        self.x += self.vel
      self.last = "d"
    if keys[pygame.K_w]:  # Check if the "w" key is pressed
      if self.y - self.vel > 20:
        self.y -= self.vel
    if keys[pygame.K_s]:  # Check if the "s" key is pressed
      if self.y + self.vel < 485:
        self.y += self.vel
    frame %= 2  # Ensure the frame index is within the valid range
    if self.last == "d":
      surface.blit(self.walkr[frame], (self.x, self.y))
    else:
      surface.blit(self.walkl[frame], (self.x, self.y))
    self.rect.center = (self.x, self.y)

  def move_joystick(self, joystick, frame,surface):
    left_stick_x = joystick.get_axis(0)
    left_stick_y = joystick.get_axis(1)

    # Adjust the Dolphin's movement based on the left joystick input
    keys = []

    if abs(left_stick_x) > 0.1:
      if left_stick_x < 0:  # Moving left
        if self.x - self.vel > 0:
          self.x -= self.vel
        self.last = "a"
      elif left_stick_x > 0:  # Moving right
        if self.x + self.vel < 750:
          self.x += self.vel
        self.last = "d"
    if abs(left_stick_y) > 0.1:
      if left_stick_y < 0:  # Moving up
        if self.y - self.vel > 0:
          self.y -= self.vel
      elif left_stick_y > 0:  # Moving down
        if self.y + self.vel < 485:
          self.y += self.vel

    frame %= 2  # Ensure the frame index is within the valid range
    if self.last == "d":
      surface.blit(self.walkr[frame], (self.x, self.y))
    else:
      surface.blit(self.walkl[frame], (self.x, self.y))
    self.rect.center = (self.x, self.y)

  def get_x(self):
    return(self.x)
  def get_y(self):
    return(self.y)

  def is_valid_move(self, x, y, maze_surface):
    rect = pygame.Rect(x, y, 30, 30)
    for row in range(20):
      for col in range(20):
        if maze_array[row * 20 + col] == 1:
          colpoint = pygame.Rect(col * 40, row * 40, 40, 40)
          if rect.colliderect(colpoint):
            return False