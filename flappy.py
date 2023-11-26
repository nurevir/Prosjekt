import pygame
from figur import Figur

class Flappy(Figur): 
    def __init__(self, bildesti: str, x:int, y:int) -> None:
        super().__init__("bilder/flappy.jpg")
        self.y_fart = 0
        self.gravitasjon = 0.3
        self.bilde = pygame.transform.scale(self.bilde, (65, 40))
        self.ramme = self.bilde.get_rect(topleft=(x, y), width=50, height=25)
        self.ramme.x = x
        self.ramme.y = y
 

    def fly(self):
        taster = pygame.key.get_pressed()
        if taster[pygame.K_SPACE]:
            print("pil opp")
            self.y_fart = -2
            self.ramme.y -= 3
        if self.ramme.y > 370:
            self.y_fart = 0
        else:
            self.y_fart += self.gravitasjon
            self.ramme.y += self.y_fart
    
    def tegn(self, vindu):
        vindu.blit(self.bilde, self.ramme)

    