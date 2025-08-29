import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Main

class Alien(Sprite):
    def __init__(self, game: "Main"):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load & scale image
        self.alien_image = pygame.image.load('./Image/alien.png')
        self.image = pygame.transform.scale_by(self.alien_image, 0.05)

        # Rect setup
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start near top-left
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Move the alien left or right."""
        self.x += (self.settings.alien_speed*self.settings.alien_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        """Return True if alien hits screen edge."""
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            return True
        return False
