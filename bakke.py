import pygame

class Bakke:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("bilder/bakke.jpg").convert_alpha()

    def beveg(self):
        self.x -= 1
        if self.x < -420:
            self.x = 0

    def tegn(self):
        vindu.blit(self.image, (self.x, self.y))