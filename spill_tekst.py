import pygame
from figur import Figur

class SpillTekst(Figur):
    def __init__(self, vindu, BREDDE, HOYDE) -> None:
        self.mellom_font = pygame.font.SysFont("Arial", 30)
        self.vindu = vindu
        self.BREDDE = BREDDE
        self.HOYDE = HOYDE
        self.poeng = 0

    def meny3(self):
        tekst_poeng = self.mellom_font.render(f"Poeng: {self.poeng}", True, (255, 255, 255))
        self.vindu.blit(tekst_poeng, (20, 60))
