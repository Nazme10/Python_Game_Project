import pygame
from settings import Settings
from ship import Ship



class Main:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(size = (
            self.settings.width,
            self.settings.height
            ))
        pygame.display.set_caption('Alien Invasion')
        self.clock = pygame.time.Clock()
        self.ship = Ship(self.screen)

         #movement flags 
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Font for FPS
        self.font = pygame.font.SysFont("Arial", 24)

    def run_game(self):
        #x =100
        #y=100
       
        while True:
            self.check_event()
            self.render()

            self.screen.fill(self.settings.bg_color)
            #self.render_fps(self.screen, self.clock, self.font)
            self.ship.blitme()
            #pygame.draw.rect(self.screen, (72, 61, 139), (100,200,200,400))
            #x+=.1
            #y+=.2
            
            pygame.display.flip()
            self.clock.tick()

    def check_event(self):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT: 
                pygame.quit()
                return
            
        #flagging
        
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_RIGHT:
                    self.moving_right = True

                elif event.key == pygame.K_LEFT:
                    self.moving_left = True

                elif event.key == pygame.K_UP:
                    self.moving_up = True

                elif event.key == pygame.K_DOWN:
                    self.moving_down = True
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.moving_right = False

                elif event.key == pygame.K_LEFT:
                    self.moving_left = False
                    
                elif event.key == pygame.K_UP:
                    self.moving_up = False

                elif event.key == pygame.K_DOWN:
                    self.moving_down = False

            
        #keys = pygame.key.get_pressed()
        # #if keys[pygame.K_UP]:
        #     self.ship.ship_rect.y -= 2
        # #if keys[pygame.K_DOWN]:
        #     self.ship.ship_rect.y += 2
        # #if keys[pygame.K_LEFT]:
        #     self.ship.ship_rect.x -= 2
        # #if keys[pygame.K_RIGHT]:
        # ##    self.ship.ship_rect.x += 2

    def render_ship(self):
        if self.moving_right == True:
                self.ship.ship_rect.x += 1
        if self.moving_left == True:
            self.ship.ship_rect.x -= 1
        if self.moving_up == True:
                self.ship.ship_rect.y -= 1
        if self.moving_down == True:
                self.ship.ship_rect.y += 1
        self.ship.blitme()

    def render(self):
            self.screen.fill(self.settings.bg_color)
            self.render_fps(self.screen, self.clock, self.font)

            
            #pygame.draw.rect(self.screen, (72, 61, 139), (100,200,200,400))
            #x+=.1
            #y+=.2
            self.render_ship()
            pygame.display.flip()
            self.clock.tick()        

    def render_fps(self,screen, clock, font):
        fps = int(clock.get_fps())
        fps_text = font.render(f"fps_rate: {fps}", True, (255, 0, 0))
        screen.blit(fps_text, (10, 10))  # Top-left corner



main = Main()
main.run_game()