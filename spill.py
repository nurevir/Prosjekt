import pygame

# 1. Oppsett

pygame.init()

#spillvindu og klokke

BREDDE = 440
HOYDE = 490
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
stor_font = pygame.font.SysFont("Arial",30)
liten_font = pygame.font.SysFont("Arial",12)

flappy_x = 175
flappy_y = 200
flappy_y_fart=0
gravitasjon = 0.1
flappy = pygame.image.load("bilder/flappy.jpg").convert_alpha()
flappy = pygame.transform.scale(flappy, (90, 55))

bakgrunn_x = 0
bakrgunn_y= 0
bakgrunn= pygame.image.load("bilder/bakgrunn1.jpg").convert_alpha()

bakke_x = 0
bakke_y = 420
bakke = pygame.image.load("bilder/bakke.jpg").convert_alpha()

while True: 

    # 2. Håndter input

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    taster = pygame.key.get_pressed()
    if taster[pygame.K_SPACE]:
        print("pil opp")
        flappy_y_fart= -2
        flappy_y -= 5
    if flappy_y > 370:
        flappy_y_fart = 0
    else:
        flappy_y_fart += gravitasjon
        flappy_y += flappy_y_fart
    if taster[pygame.K_ESCAPE]:
        pygame.quit()
        raise SystemExit
    
    # 3. Opddater spill
    bakke_x -= 1
    if bakke_x <- 420:
        bakke_x = 0

    # 4. Tegn (print)
    vindu.fill("white")

    vindu.blit(bakgrunn, (bakgrunn_x,bakrgunn_y))
    vindu.blit(bakke,(bakke_x,bakke_y))
    
    vindu.blit(flappy, (flappy_x,flappy_y))

    tekst = stor_font.render("Flappy bird", True, "white")
    vindu.blit(tekst,(20,20))

    print("En runde i gameloopen")
    pygame.display.flip()
    klokke.tick(FPS)