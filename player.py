import pygame
from constants import *

class Player(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
        """
        Player constructor. 
        """
        super().__init__()

        self.movex = 0
        self.movey = 0

        self.image = pygame.transform.scale(PLAYER_IMG, (width, height))
        
        # Fetch the rectangle object that has the dimensiton of the image
        # Update the position the object by setting values of
        # rect.x and rect.y
        self.rect = self.image.get_rect()

    def control(self, x, y):
        """
        Control player movement
        """
        self.movex += x
        self.movey += y

    def update(self):
        """
        Update sprite position
        """
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey