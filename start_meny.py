import pygame
from figur import Figur

class StartMeny(Figur):
    def __init__(self, vindu, BREDDE, HOYDE) -> None:
        self.overskrift = pygame.font.SysFont("Arial", 50)
        self.mellom_font = pygame.font.SysFont("Arial", 30)
        self.vindu = vindu
        self.BREDDE = BREDDE
        self.HOYDE = HOYDE

    def meny1(self):
        tekst_start = self.mellom_font.render("Trykk SPACE for å starte", True, (255, 255, 255))
        self.vindu.blit(tekst_start, (self.BREDDE // 2 - tekst_start.get_width() // 2, self.HOYDE // 2 - tekst_start.get_height() // 2))
        tekst_flappy = self.overskrift.render("Flappy bird", True, (255, 255, 255))
        self.vindu.blit(tekst_flappy, (20, 20))
