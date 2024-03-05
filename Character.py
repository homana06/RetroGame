import pygame
import time
from Maze import *
screen = (800, 600)


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
    self.jump_cooldown = 2  # Cooldown time in seconds
    self.last_jump_time = 0  # Time when the last jump occurred
    self.jumping = False  # Flag to track if the player is currently jumping
    self.max_jump_vel = 10  # Maximum upward velocity during jump

  def draw(self, surface):
    #pygame.draw.rect(surface, (0,0,255), self.rect)
    if self.last == "a":
      surface.blit(self.walkl[0], (self.x, self.y))
    else:
      surface.blit(self.walkr[0], (self.x, self.y))

  def is_valid_move(self, x, y,maze_array):
    rect = pygame.Rect(x, y, 30, 30)
    for row in range(len(maze_array)):
      for col in range(len(maze_array[0])):
        if maze_array[row][col] == 1:
          colpoint1 = pygame.Rect(col * 40, row * 28, 30, 30)
          colpoint2 = pygame.Rect(col * 35, row * 35, 30, 30)
          if rect.colliderect(colpoint1) or rect.colliderect(colpoint2):
            return False
    return True

  def move(self, keys, frame, surface,maze_array):
    # Always try to fall downwards
    new_y = self.y + self.vel
    if new_y + self.rect.height < 700:  # Check if falling won't go beyond the bottom boundary
      if self.is_valid_move(self.x, new_y,maze_array):
        self.y = new_y

    if keys[pygame.K_a]:  # Check if the "a" key is pressed
      if self.x - self.vel > 0:
        new_x = self.x - self.vel
        if self.is_valid_move(new_x, self.y,maze_array):
          self.x = new_x
      self.last = "a"
    if keys[pygame.K_d]:  # Check if the "d" key is pressed
      if self.x + self.vel < 725:
        new_x = self.x + self.vel
        if self.is_valid_move(new_x, self.y,maze_array):
          self.x = new_x
      self.last = "d"
    if keys[pygame.K_SPACE]:  # Check if the space bar is held down
      if not self.jumping:  # If the player is not currently jumping
        self.jumping = True
        self.jump_start_y = self.y  # Record the starting position of the jump

      if self.vel < self.max_jump_vel:  # Increase velocity until it reaches maximum
        self.vel += 1

    else:  # Space bar is released
      if self.jumping:  # If the player was jumping
        self.jumping = False
        self.vel = 1  # Reset velocity for the next jump

    if self.jumping:  # If the player is currently jumping
      new_y = self.y - 5 * self.vel  # Calculate new y-coordinate based on velocity
      if new_y > 20:  # Check if the jump won't go beyond the top boundary
        if self.is_valid_move(self.x, new_y, maze_array):
          self.y = new_y
      else:  # Reached the maximum height of the jump, start descending
        self.jumping = False
        self.vel = 1  # Reset velocity for the next jump

    frame %= 2  # Ensure the frame index is within the valid range
    if self.last == "d":
      surface.blit(self.walkr[frame], (self.x, self.y))
    else:
      surface.blit(self.walkl[frame], (self.x, self.y))
    self.rect.center = (self.x, self.y)

  def move_joystick(self, joystick, frame, surface):
    left_stick_x = joystick.get_axis(0)
    left_stick_y = joystick.get_axis(1)

    # Adjust the Dolphin's movement based on the left joystick input
    keys = []

    if abs(left_stick_x) > 0.1:
      if left_stick_x < 0:  # Moving left
        new_x = self.x - self.vel
        if self.is_valid_move(new_x, self.y):
          self.x = new_x
        self.last = "a"
      elif left_stick_x > 0:  # Moving right
        new_x = self.x + self.vel
        if self.is_valid_move(new_x, self.y):
          self.x = new_x
        self.last = "d"
    if abs(left_stick_y) > 0.1:
      if left_stick_y < 0:  # Moving up
        new_y = self.y - self.vel
        if self.is_valid_move(self.x, new_y):
          self.y = new_y
      elif left_stick_y > 0:  # Moving down
        new_y = self.y + self.vel
        if self.is_valid_move(self.x, new_y):
          self.y = new_y

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
