import pygame, sys
from entities.player import Player
from entities.bricks import Bricks
from entities.ball import Ball
from constants import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Brick pong")
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.bricks = Bricks()
        self.ball = Ball()
        self.movement = 0

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and self.movement < 0:
                        self.movement = 0
                    if event.key == pygame.K_RIGHT and self.movement > 0:
                        self.movement = 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement = -1
                    if event.key == pygame.K_RIGHT:
                        self.movement = 1

            self.screen.fill("gray")

            self.player.update(self.movement)
            self.player.render(self.screen)

            self.bricks.render(self.screen)

            self.ball.update(self.player, self.bricks.grid)
            self.ball.render(self.screen)

            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    Game().run()