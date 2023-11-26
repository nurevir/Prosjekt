import pygame
from flappy import Flappy
from bakke import Bakke
from bakgrunn import Bakgrunn
from pipe import Pipe
from start_meny import StartMeny
from slutt_meny import SluttMeny
from spill_tekst import SpillTekst

# 1. Oppsett
pygame.init()

BREDDE = 440
HOYDE = 490
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
poeng = 0

## Oppretter objekter
flappy = Flappy("bilder/flappy.jpg", 190, 200)
bakgrunn = Bakgrunn("bilder/bakgrunn1.jpg", 0, 0)
bakke = Bakke("bilder/bakke.jpg", 0, 420)
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

## Meny
start_meny = StartMeny(vindu, BREDDE, HOYDE)
slutt_meny = SluttMeny(vindu, BREDDE, HOYDE)
spill_tekst = SpillTekst(vindu, BREDDE, HOYDE)

## Spilltilstander
MENY = 0
SPILL_AKTIV = 1
SPILL_OVER = 2
spilltilstand = MENY

while True:
    # 2. Håndterer input
    vindu.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if spilltilstand == MENY or spilltilstand == SPILL_OVER:
                    spilltilstand = SPILL_AKTIV 
                    poeng = 0
                elif spilltilstand == SPILL_AKTIV:
                    flappy.fly()
    
    if spilltilstand == MENY: # Start meny vises med engang
        ## tegner 
        bakgrunn.tegn(vindu)
        bakke.beveg()
        bakke.tegn(vindu)

        start_meny.meny1()

    elif spilltilstand == SPILL_AKTIV: # Spillet er i gang
        for pipe in pipes:
            if flappy.ramme.colliderect(pipe.ramme):
                spilltilstand = SPILL_OVER
            if pipe.ramme < flappy.ramme:
                pipe.passert = True
                if spilltilstand != SPILL_OVER:
                    spill_tekst.poeng += 1
                    slutt_meny.poeng += 1
                    print(f"Score: {poeng}")
        ## tegner 
        bakgrunn.tegn(vindu)
        bakke.tegn(vindu)
        flappy.tegn(vindu)

        ## Oppdaterer
        bakke.beveg()
        flappy.fly()
        for pipe in pipes:
            pipe.beveg()
            pipe.tegn(vindu)

        spill_tekst.meny3()

    elif spilltilstand == SPILL_OVER: # Spillet er over
        ## tegner 
        bakgrunn.tegn(vindu)
        bakke.tegn(vindu)
       
        ## Oppdaterer
        bakke.beveg()
        slutt_meny.meny2()
        
        ## Trykk på space for å starte spillet om igjen
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            spilltilstand = SPILL_AKTIV
            ## nullstiller poengene
            spill_tekst.poeng = 0
            slutt_meny.poeng = 0

             ## Setter pipene i start-posisjon
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
            ## Setter flappy i start-posisjon
            flappy = Flappy("bilder/flappy.jpg", 190, 200)

    pygame.display.flip()
    klokke.tick(FPS)
