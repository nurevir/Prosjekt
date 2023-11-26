import pygame

def game_over_menu():
    poeng = 0
    stor_font = pygame.font.SysFont("Arial", 30)
    liten_font = pygame.font.SysFont("Arial", 12) 
    game_over_text = stor_font.render("Game Over", True, "red")
    score_text = stor_font.render(f"Score: {poeng}", True, "white")

    restart_text = liten_font.render("Press R to restart", True, "black")
    exit_text = liten_font.render("Press ESC to exit", True, "black")

    vindu.blit(game_over_text, (BREDDE // 2 - game_over_text.get_width() // 2, HOYDE // 2 - 50))
    vindu.blit(score_text, (BREDDE // 2 - score_text.get_width() // 2, HOYDE // 2))
    vindu.blit(restart_text, (BREDDE // 2 - restart_text.get_width() // 2, HOYDE // 2 + 50))
    vindu.blit(exit_text, (BREDDE // 2 - exit_text.get_width() // 2, HOYDE // 2 + 80))

