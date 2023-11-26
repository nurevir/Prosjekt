import pygame
from figur import Figur


class Pipe(Figur):
    def __init__(self, image_path, x, y):
        super().__init__(image_path)
        self.fart = -2
        self.ramme = self.bilde.get_rect(topleft=(x, y))
        self.passert = False 

    def beveg(self):
        self.ramme.x += self.fart
        if self.ramme.x < 0:  
            self.ramme.x = 600 
    
    def reset(self):
        self.x = 440
        self.y = 0
        self.passert = False

    def tegn(self, vindu):
        vindu.blit(self.bilde, self.ramme)
        
