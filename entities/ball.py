import pygame
from constants import *


class Ball:
    def __init__(self, radius = 10, color = (255, 0, 0)):
        self.x = WINDOW_SIZE[0] // 2
        self.y = WINDOW_SIZE[1] // 2
        self.radius = radius
        self.color = color
        self.vel_x = 2
        self.vel_y = 10

    def render(self, surf):
        pygame.draw.circle(surf, self.color, (self.x, self.y), self.radius)

    def update(self, player, grid):
        if self.x <= 0 + self.radius or self.x >= WINDOW_SIZE[0] - self.radius:
            self.vel_x *= -1
        if self.y <= 0 + self.radius:
            self.vel_y *= -1
        if self.y >= WINDOW_SIZE[1]:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
        if self.y >= player.y - self.radius and player.x <= self.x <= player.x + player.width:
            self.vel_y *= -1

        todelete = []
        for key in grid:
            if grid[key].ball_collision(self):
                self.vel_y *= -1
                todelete.append(key)
        for key in todelete:
            del grid[key]

        self.x += self.vel_x
        self.y += self.vel_y
