import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        self.setting = game.settings
        self.ship = game.ship

        self.rect = pygame.Rect(0,0,25,50)
        self.rect.midtop = self.ship.ship_rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= 1
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, (48, 6, 3), self.rect)