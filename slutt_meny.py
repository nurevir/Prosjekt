import pygame
from figur import Figur

class SluttMeny(Figur):
    def __init__(self, vindu: int, BREDDE:int, HOYDE:int) -> None:
        self.stor_font = pygame.font.SysFont("Arial", 50)
        self.mellom_font = pygame.font.SysFont("Arial", 30)
        self.liten_font = pygame.font.SysFont("Arial", 20)
        self.vindu = vindu
        self.BREDDE = BREDDE
        self.HOYDE = HOYDE
        self.poeng = 0

    def meny2(self):
        tekst = self.stor_font.render("Game Over", True, ("Red"))
        self.vindu.blit(tekst, (self.BREDDE // 2 - tekst.get_width() // 2, 180))
        tekst_poeng = self.mellom_font.render(f"Poeng: {self.poeng}", True, ("White"))
        self.vindu.blit(tekst_poeng, ((self.BREDDE // 2 - tekst_poeng.get_width() // 2, 240)))
        tekst_start_på_nytt = self.liten_font.render("Trykk SPACE for å spille igjen", True, ("White"))
        self. vindu.blit(tekst_start_på_nytt, ((self.BREDDE // 2 - tekst_start_på_nytt.get_width() // 2, 280)))