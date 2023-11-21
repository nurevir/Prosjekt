import pygame
from figur import Figur

class Bakke(Figur): 
    def __init__(self, bildesti: str, x: int, y:int) -> None:
        super().__init__("bilder/bakke.jpg")
        self.x = x
        self.y = y
      
    def beveg(self):
        self.x -= 1
        if self.x < -420:
            self.x = 0

    def tegn(self,vindu: pygame.Surface):
        vindu.blit(self.bilde,(self.x, self.y))