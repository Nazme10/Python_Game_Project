import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
 from main import Main

class Alien(Sprite):
 def __init__(self,game:"Main"):
   super().__init__()
   self.screen = game.screen
   self.alien_image = pygame.image.load('./Image/alien.png')
   self.image = pygame.transform.scale_by(self.alien_image, .09)

#scale the alien image
   #scale_factor = 0.05
  # original_size = self.alien_image.get_size()
   #scaled_size = (int(original_size[0] * scale_factor), int (original_size[1] * scale_factor))
   #self.image =pygame.transform.scale(self.alien_image, scaled_size)

#set the rect for the alien
   self.rect = self.image.get_rect()
   self.screen_rect = self.screen.get_rect()


   self.rect.topleft = self.screen_rect.topleft
   self.x = float(self.rect.x)
   self.y = float(self.rect.y)
  

 