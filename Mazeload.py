import pygame

from Maze import *
collide = pygame.Surface((800,800), pygame.SRCALPHA)
collide.fill((0, 0, 0, 0))

class Maze():
    def __init__(self,maze1,maze2,maze3,maze4):
        self.maze1 = maze1
        self.maze2 = maze2
        self.maze3 = maze3
        self.maze4 = maze4
        self.x = 1
        self.y = 1
        self.collide = collide
        self.doorcoordinates = []
        self.maze_array = maze1
        self.startx = 0



    def mazeload(self, screen, background_width, background_height):
        # Calculate the size of each maze cell dynamically
        cell_width = background_width / len(self.maze_array[0])
        cell_height = background_height / len(self.maze_array)

        for row in range(len(self.maze_array)):
            for col in range(len(self.maze_array[0])):
                cell_value = self.maze_array[row][col]
                screen = None
                if cell_value == 1:  # Assuming 1 represents a wall
                    wall = pygame.image.load("images/Testwall1.png")
                    # Scale the wall image to fit the cell size
                    wall = pygame.transform.scale(wall, (int(cell_width), int(cell_height)))
                    wall_rect = wall.get_rect()
                    # Calculate the position of the cell on the screen
                    wall_rect.topleft = col * cell_width, row * cell_height
                    collide.blit(wall, wall_rect)
                elif cell_value == 2:
                    wall = pygame.image.load("images/TempDoor.png")
                    # Scale the wall image to fit the cell size
                    wall = pygame.transform.scale(wall, (int(cell_width), int(cell_height)))
                    wall_rect = wall.get_rect()
                    # Calculate the position of the cell on the screen
                    wall_rect.topleft = col * cell_width, row * cell_height
                    collide.blit(wall, wall_rect)
                    self.doorcoordinates.append((col * cell_width, row * cell_height))

    def set_pos(self,x,y):
        self.x = x
        self.y = y

    def get_mazetype(self):
        return(self.maze_array)

    def mapidentify(self):
        # Iterate through door coordinates to check if player position matches
        for door_coord in self.doorcoordinates:
            if (self.x, self.y) == door_coord:
                # Compare x and y components separately
                if door_coord[0] >= 710:
                    self.startx += 1
                    self.mapload()
                elif door_coord[0] <= 10:
                    self.startx -= 1
                    self.mapload()

    def mapload(self):
        if self.startx == 0:
            self.maze_array = maze1
        elif self.startx == 1:
            self.maze_array = maze2
        elif self.startx == 2:
            self.maze_array = maze3
        elif self.startx == 3:
            self.maze_array = maze4

