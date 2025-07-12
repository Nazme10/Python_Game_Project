class Ship:
    def __init__(self,screen):
        ship_image = pygame.image.load('./Image/spaceship.png')
        self.ship_image = pygame.transform.scale_by(ship_image, .07)
        self.screen=screen

    def blitme(self):
        self.screen.blit(self.ship_image,(550,350))