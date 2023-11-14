import pygame
from figur import Figur

class Bakgrunn(Figur):
    def __init__(self, x: int, y:int) -> None:
        super().__init__("bilder/bakgrunn1.jpg")
        self.x = x
        self.y = y
    
