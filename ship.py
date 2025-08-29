import pygame
from settings import Settings

class Ship:
    def __init__(self,screen):
        ship_image = pygame.image.load('./Image/spaceship.png')
        self.ship_image = pygame.transform.scale_by(ship_image, .11)
        self.settings = Settings()
        self.screen=screen

        self.rect = self.ship_image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 10

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #movement flags 
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left == True and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x
        if self.moving_up == True and self.rect.top > self.screen_rect.top:
                self.y -= self.settings.ship_speed
        if self.moving_down == True and self.rect.bottom < self.screen_rect.bottom:
                self.y += self.settings.ship_speed

        self.rect.y = self.y
        


    def blitme(self):
        self.screen.blit(self.ship_image,self.rect)