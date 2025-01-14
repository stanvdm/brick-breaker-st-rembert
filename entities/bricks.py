import pygame
from constants import *

class Brick:
    def __init__(self, x, y, size = (100, 40), color = (255, 0, 0)):
        self.x = x
        self.y = y
        self.width = size[0]
        self.height = size[1]
        self.color = color

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def render(self, surf):
        pygame.draw.rect(surf, self.color, self.rect())
    
    def ball_collision(self, ball):
        if not (ball.x <= self.x + self.width and ball.x >= self.x):
            return False
        if not (ball.y - ball.radius <= self.y + self.height):
            return False
        return True

class Bricks:
    def __init__(self, gap = 10, grid_size = (8, 4)):
        self.grid_size = grid_size
        self.gap = gap
        self.grid = {}
        self.brick_size = (100, 40)
        x_offset = (WINDOW_SIZE[0] - self.grid_size[0] * self.brick_size[0] - gap * (grid_size[0] - 1)) // 2
        self.pos = (x_offset, 20)
        self.init_grid()
        
    def init_grid(self):
        y_pos = self.pos[1]
        for y in range(self.grid_size[1]):
            x_pos = self.pos[0]
            for x in range(self.grid_size[0]):
                self.grid[f"{x};{y}"] = Brick(x_pos, y_pos, size=self.brick_size)
                x_pos += self.brick_size[0] + self.gap
            y_pos += self.brick_size[1] + self.gap
    
    def render(self, surf):
        for _, brick in self.grid.items():
            brick.render(surf)

    def update(self):
        pass