import random
from figur import Figur

class Ball(Figur):
    def __init__(self, vindu_bredde: int):
        super().__init__("bilder/ball.png")

        # Flytter ballen til startposisjonen
        self.ramme.centerx = random.randint(0, vindu_bredde)
        self.ramme.top = 0

    def fall(self, vindu_høyde: int):
        self.ramme.y += 6
        if self.ramme.top > vindu_høyde:
            self.ramme.centerx = random.randint(0, 800)
            self.ramme.y = 0

