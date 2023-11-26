import pygame
from flappy import Flappy
from bakke import Bakke
from bakgrunn import Bakgrunn
from pipe import Pipe

pygame.init()

BREDDE = 440
HOYDE = 490
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

stor_font = pygame.font.SysFont("Arial", 30)
liten_font = pygame.font.SysFont("Arial", 12)

poeng = 0

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

        tekst_start = stor_font.render("Trykk SPACE for å starte", True, ("White"))
        vindu.blit(tekst_start, (BREDDE // 2 - tekst_start.get_width() // 2, HOYDE // 2 - tekst_start.get_height() // 2))
        tekst_flappy = stor_font.render("Flappy bird", True, ("White"))
        vindu.blit(tekst_flappy, (20, 20))

    elif game_mode == GAME_ACTIVE:
        for pipe in pipes:
            if flappy.ramme.colliderect(pipe.ramme):
                game_mode = GAME_OVER

            if pipe.ramme < flappy.ramme:
                pipe.passert = True
                if game_mode != GAME_OVER:
                    poeng += 1
                    print(f"Score: {poeng}")

        bakgrunn.tegn(vindu)
        bakke.beveg()
        bakke.tegn(vindu)

        flappy.fly()
        flappy.tegn(vindu)

        for pipe in pipes:
            pipe.beveg()
            pipe.tegn(vindu)

        tekst_poeng = stor_font.render(f"Poeng: {poeng}", True, (255, 255, 255))
        vindu.blit(tekst_poeng, (20, 60))

    elif game_mode == GAME_OVER:
        bakgrunn.tegn(vindu)
        bakke.beveg()
        bakke.tegn(vindu)

        tekst = stor_font.render("Game Over", True, (255, 0, 0))
        vindu.blit(tekst, (BREDDE // 2 - tekst.get_width() // 2, HOYDE // 2 - tekst.get_height() // 2))
        tekst_poeng = stor_font.render(f"Poeng: {poeng}", True, (255, 0, 0))
        vindu.blit(tekst_poeng, ((BREDDE // 2 - tekst.get_width() // 2, 270)))

        # Check for space bar press to restart the game
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game_mode = GAME_ACTIVE
            poeng = 0

    pygame.display.flip()
    klokke.tick(FPS)
