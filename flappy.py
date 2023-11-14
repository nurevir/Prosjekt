import pygame

class Flappy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.y_fart = 0
        self.gravitasjon = 0.1
        self.image = pygame.image.load("bilder/flappy.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (90, 55))

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

    def tegn(self):
        vindu.blit(self.image, (self.x, self.y))
