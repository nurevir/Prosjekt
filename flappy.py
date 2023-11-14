import pygame
from figur import Figur

class Flappy(Figur): 
    def __init__(self,x: int, y:int) -> None:
        super().__init__("bilder/flappy.jpg")
        #  self.image = pygame.transform.scale(self.image, (90, 55))
        self.x = x
        self.y = y
        self.y_fart = 0
        self.gravitasjon = 0.1

    def fly(self):
        taster = pygame.key.get_pressed()
        if taster[pygame.K_SPACE]:
            print("pil opp")
            self.y_fart = -2
            self.y -= 5
        if self.y > 370:
            self.y_fart = 0
        else:
            self.y_fart += self.gravitasjon
            self.y += self.y_fart

    def tegn(self, vindu):
        vindu.blit(self.image, (self.x, self.y))