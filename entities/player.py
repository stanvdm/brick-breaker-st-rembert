import pygame
from constants import *

class Player:
    def __init__(self):
        self.width = 200
        self.height = 20
        self.x = (WINDOW_SIZE[0] // 2) - (self.width // 2)
        self.y = WINDOW_SIZE[1] - (self.height * 2)
        self.velocity = 10

    def render(self, surf):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(surf, (255, 0, 0), rect)

    def update(self, movement = 0):
        if movement == 0:
            self.velocity = 10
        self.velocity = min(20, self.velocity * 1.1)
        self.x += self.velocity * movement

        if self.x < 0:
            self.x = 0
        if self.x > WINDOW_SIZE[0] - self.width:
            self.x = WINDOW_SIZE[0] - self.width
