class Bakgrunn:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("bilder/bakgrunn1.jpg").convert_alpha()

    def tegn(self):
        vindu.blit(self.image, (self.x, self.y))
