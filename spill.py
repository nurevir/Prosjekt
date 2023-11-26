import pygame

## importerer klasser 
from flappy import Flappy
from bakke import Bakke
from bakgrunn import Bakgrunn
from pipe import Pipe

## 1. ppsett
pygame.init()

# spillvindu og klokke
BREDDE = 440
HOYDE = 490
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

# font
stor_font = pygame.font.SysFont("Arial", 30)
liten_font = pygame.font.SysFont("Arial", 12) 

## Opprett objekter
poeng = 0

# flappy
flappy = Flappy("bilder/flappy.jpg", 190, 200)

# bakgrunn
bakgrunn = Bakgrunn("bilder/bakgrunn1.jpg",0, 0)

# bakke (som beveger seg)
bakke = Bakke("bilder/bakke.jpg", 0, 420)

# liste for de ulike pipene
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

# spill-løkke
game_over = False
game_started = False 

while True:
    # 2. håndter input
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


    # 3.Oppdater spill
    if game_started:  # sjekker om spillet har startet
        for pipe in pipes:
            if flappy.ramme.colliderect(pipe.ramme): #sjekker om flappy kolliderer med pipene
                game_over = True # om de kolliderer er det game over
                print("Game over")
            if pipe.ramme.width < flappy.ramme.x: 
                pipe.passert = True
                if not game_over: # får kun poeng hvis det ikke er game over
                    poeng += 1
                    print(f"Score: {poeng}")
                
    # 4.Tegn (print)
        vindu.fill("white")
        bakgrunn.tegn(vindu)

        # Flappy bird tekst
        tekst_flappy = stor_font.render("Flappy bird", True, "white")
        vindu.blit(tekst_flappy, (20, 20))

        if not game_over: # tegnes kun når det ikke er game over
            # funksjoner
            flappy.fly()
            bakke.beveg()
            for pipe in pipes:
                pipe.beveg()

            # tegner alle objektene i spillet
            bakke.tegn(vindu)
            flappy.tegn(vindu)
            for pipe in pipes:
                pipe.tegn(vindu)

            if game_started: # poengsum vises når spillet settes igang
                tekst_poeng = stor_font.render(f"Poeng: {poeng}", True, "white")
                vindu.blit(tekst_poeng, (20, 60))
        else:
            # hvis det er game over
            tekst = stor_font.render("Game Over", True, "red")
            vindu.blit(tekst, (BREDDE // 2 - tekst.get_width() // 2, HOYDE // 2 - tekst.get_height() // 2))
            tekst_poeng = stor_font.render(f"Poeng: {poeng}", True, "red")
            vindu.blit(tekst_poeng, ((BREDDE // 2 - tekst.get_width() // 2, 270)))

    pygame.display.flip()
    klokke.tick(FPS)
