import pygame
from flappy import Flappy
from bakke import Bakke
from bakgrunn import Bakgrunn
from pipe import Pipe
from start_meny import StartMeny
from slutt_meny import SluttMeny
from spill_tekst import SpillTekst

pygame.init()

BREDDE = 440
HOYDE = 490
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

poeng = 0

flappy = Flappy("bilder/flappy.jpg", 190, 200)
bakgrunn = Bakgrunn("bilder/bakgrunn1.jpg", 0, 0)
bakke = Bakke("bilder/bakke.jpg", 0, 420)
start_meny = StartMeny(vindu, BREDDE, HOYDE)
slutt_meny = SluttMeny(vindu, BREDDE, HOYDE)
spill_tekst = SpillTekst(vindu, BREDDE, HOYDE)

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

MENU = 0
GAME_ACTIVE = 1
GAME_OVER = 2
game_mode = MENU

while True:
    vindu.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_mode == MENU or game_mode == GAME_OVER:
                    game_mode = GAME_ACTIVE
                    poeng = 0
                elif game_mode == GAME_ACTIVE:
                    flappy.fly()

    if game_mode == MENU:
        bakgrunn.tegn(vindu)
        bakke.beveg()
        bakke.tegn(vindu)

        start_meny.meny1()

    elif game_mode == GAME_ACTIVE:
        for pipe in pipes:
            if flappy.ramme.colliderect(pipe.ramme):
                game_mode = GAME_OVER
            if pipe.ramme < flappy.ramme:
                pipe.passert = True
                if game_mode != GAME_OVER:
                    spill_tekst.poeng += 1
                    slutt_meny.poeng += 1
                    print(f"Score: {poeng}")

        bakgrunn.tegn(vindu)
        bakke.beveg()
        bakke.tegn(vindu)

        flappy.fly()
        flappy.tegn(vindu)

        for pipe in pipes:
            pipe.beveg()
            pipe.tegn(vindu)

        spill_tekst.meny3()

    elif game_mode == GAME_OVER:
        bakgrunn.tegn(vindu)
        bakke.beveg()
        bakke.tegn(vindu)
        
        slutt_meny.meny2()
        
        # Check for space bar press to restart the game
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game_mode = GAME_ACTIVE
            spill_tekst.poeng = 0
            slutt_meny.poeng = 0

        # Reset pipes to initial positions
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
        
            flappy = Flappy("bilder/flappy.jpg", 190, 200)

    pygame.display.flip()
    klokke.tick(FPS)
