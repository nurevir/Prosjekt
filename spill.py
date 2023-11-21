import pygame

## importerer klasser
from flappy import Flappy
from bakke import Bakke
from bakgrunn import Bakgrunn
from pipe import Pipe
from meny import Meny

## Oppsett
pygame.init()

## Spillvindu og klokke
BREDDE = 440
HOYDE = 490
FPS = 60
poeng = 0
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
stor_font = pygame.font.SysFont("Arial", 30)
liten_font = pygame.font.SysFont("Arial", 12) 
font = pygame.font.SysFont("Arial", 20)


## Opprett objekter
#meny
meny = Meny()


# flappy
flappy = Flappy("bilder/flappy.jpg", 190, 200)

# bakgrunn
bakgrunn = Bakgrunn("bilder/bakgrunn1.jpg",0, 0)

# bakke ( som beveger seg)
bakke = Bakke("bilder/bakke.jpg", 0, 420)

# liste for pipene
pipes = [
    Pipe("bilder/pipe1.png", 50, 320),
    Pipe("bilder/pipe2.png", 200, 290),
    Pipe("bilder/pipe3.png", 50, 0),
    Pipe("bilder/pipe4.png", 200, 0),
    Pipe("bilder/pipe4.png", 350, 0),
    Pipe("bilder/pipe6.png", 350, 280),
    Pipe("bilder/pipe7.png", 500, 0),
    Pipe("bilder/pipe8.png", 500, 380),
]

## Spill-løkke
game_over = False
game_started = False 
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
            if event.key == pygame.K_SPACE:
                game_started = True  # spillet starter når SPACE-tasten trykkes på

    ## Oppdater spill
    if game_started:  # sjekker om spillet har startet
        for pipe in pipes:
            if flappy.ramme.colliderect(pipe.ramme):
                game_over = True
                print("Game over")
            if pipe.ramme.x + pipe.ramme.width < flappy.ramme.x and not pipe.passert:
                pipe.passert = True
                poeng += 1
                print(f"Score: {poeng}")

        flappy.fly()
        bakke.beveg()
        for pipe in pipes:
            pipe.beveg()

    ## Tegn (print)
    vindu.fill("white")

    if not game_over:
        bakgrunn.tegn(vindu)
        bakke.tegn(vindu)
        flappy.tegn(vindu)

        for pipe in pipes:
            pipe.tegn(vindu)

        tekst_flappy = stor_font.render("Flappy bird", True, "white")
        vindu.blit(tekst_flappy, (20, 20))

        if game_started:
            tekst_poeng = stor_font.render(f"Poeng: {poeng}", True, "white")
            vindu.blit(tekst_poeng, (20, 60))
        else:
          Meny.tegn_start(vindu)
    else:
        Meny.tegn_slutt(vindu,poeng)
        
    pygame.display.flip()
    klokke.tick(FPS)