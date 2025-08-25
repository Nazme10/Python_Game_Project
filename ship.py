import pygame
from settings import Settings

class Ship:
    def __init__(self,screen):
        ship_image = pygame.image.load('./Image/spaceship.png')
        self.ship_image = pygame.transform.scale_by(ship_image, .07)
        self.settings = Settings()
        self.screen=screen
        self.ship_rect = self.ship_image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.ship_rect.midbottom = self.screen_rect.midbottom
        self.ship_rect.y -= 30

        #movement flags 
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right == True:
                self.ship_rect.x += self.settings.ship_speed
        if self.moving_left == True:
            self.ship_rect.x -= self.settings.ship_speed
        if self.moving_up == True:
                self.ship_rect.y -= self.settings.ship_speed
        if self.moving_down == True:
                self.ship.ship_rect.y += self.settings.ship_speed
        self.blitme()


    def blitme(self):
        self.screen.blit(self.ship_image,self.ship_rect)