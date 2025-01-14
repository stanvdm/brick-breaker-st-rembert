import pygame
from constants import *

class Player:
    def __init__(self):
        self.width = 200
        self.height = 20
        self.x = (WINDOW_SIZE[0] // 2) - (self.width // 2)
        self.y = WINDOW_SIZE[1] - (self.height * 2)
        self.velocity = PLAYER_SPEED

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def render(self, surf):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(surf, (255, 0, 0), rect)

    def update(self, movement = 0):
        self.x += self.velocity * movement

        if self.x < 0:
            self.x = 0
        if self.x > WINDOW_SIZE[0] - self.width:
            self.x = WINDOW_SIZE[0] - self.width
