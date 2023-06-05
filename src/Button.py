import pygame
from helper import load_image

class Button:
    def __init__(self, file, screen):
        self.screen = screen
        self.image = load_image(file)
        self.x = 0 
        self.y = 0
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def set_coords(self, x, y):
        self.x = x 
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        self.screen.blit(self.image, (self.image, self.image))

    def resize(self, x, y):
        self.image = pygame.transform.scale(self.image, (x, y))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def resize_mult(self, mult):
        self.width = self.image.get_width() * mult
        self.height = self.image.get_height() * mult
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)