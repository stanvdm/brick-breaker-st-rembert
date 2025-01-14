import pygame, math
from constants import *


class Ball:
    def __init__(self, radius = 10, color = (255, 0, 0)):
        self.x = WINDOW_SIZE[0] // 2
        self.y = WINDOW_SIZE[1] // 2
        self.radius = radius
        self.color = color
        self.vel_x = 0
        self.vel_y = BALL_SPEED

    def render(self, surf):
        pygame.draw.circle(surf, self.color, (self.x, self.y), self.radius)

    def collision_with_rect(self, rect):        
        distance_x = self.x - max(rect.left, min(self.x, rect.right))
        distance_y = self.y - max(rect.top, min(self.y, rect.bottom))
        
        return (distance_x ** 2) + (distance_y ** 2) < (self.radius ** 2)

    def update(self, player, grid):
        if self.x <= self.radius or self.x >= WINDOW_SIZE[0] - self.radius:
            self.vel_x *= -1
        if self.y <= self.radius:
            self.vel_y *= -1
        if self.y >= WINDOW_SIZE[1]:
            pygame.event.post(pygame.event.Event(pygame.QUIT))

        # player collision
        if self.collision_with_rect(player.rect()):
            paddle_center = player.x + player.width/2
            angle = math.radians((self.x - paddle_center) * 90 / player.width)
            self.vel_x = math.sin(angle) * BALL_SPEED
            self.vel_y = - math.cos(angle) * BALL_SPEED

        todelete = []
        for key in grid:
            if self.collision_with_rect(grid[key].rect()):
                self.vel_y *= -1
                todelete.append(key)
        for key in todelete:
            del grid[key]

        self.x += self.vel_x
        self.y += self.vel_y
