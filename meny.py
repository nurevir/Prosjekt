import pygame
import sys
from figur import Figur

class Meny(Figur):
    def __init__(self, width, height, font_size) -> None:
        self.width = width
        self.height = height
        self.font_size = font_size
        self.font = pygame.font.SysFont("Arial", self.font_size)

    def tegn_start(self, vindu):
        velkomst_tekst = self.font.render("Velkommen til Flappy Bird!", True, "black")
        start_tekst = self.font.render("Trykk SPACE for å starte", True, "black")
        vindu.blit(velkomst_tekst, (self.width // 2 - velkomst_tekst.get_width() // 2, 100))
        vindu.blit(start_tekst, (self.width // 2 - start_tekst.get_width() // 2, 150))

    def tegn_slutt(self, vindu, poeng):
        game_over_tekst = self.font.render("Game Over", True, "red")
        poeng_tekst = self.font.render(f"Poeng: {poeng}", True, "red")
        vindu.blit(game_over_tekst, (self.width // 2 - game_over_tekst.get_width() // 2, 100))
        vindu.blit(poeng_tekst, (self.width // 2 - poeng_tekst.get_width() // 2, 150))



