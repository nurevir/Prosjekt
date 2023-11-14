import pygame
from flappy import Flappy
from bakke import Bakke
from bakgrunn import Bakgrunn

# 1. Oppsett
pygame.init()

# Spillvindu og klokke
BREDDE = 440
HOYDE = 490
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
stor_font = pygame.font.SysFont("Arial", 30)
liten_font = pygame.font.SysFont("Arial", 12)


# Opprett objekter
flappy = Flappy(175, 200)
bakgrunn = Bakgrunn(0, 0)
bakke = Bakke(0, 420)

# Spill-løkke
while True:
    # Håndter input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                raise SystemExit

    # Oppdater spill
    flappy.fly()
    bakke.beveg()

    # Tegn (print)
    vindu.fill("white")
    bakgrunn.tegn()
    bakke.tegn()
    flappy.tegn()

    tekst = stor_font.render("Flappy bird", True, "white")
    vindu.blit(tekst, (20, 20))

    print("En runde i gameloopen")
    pygame.display.flip()
    klokke.tick(FPS)