import pygame
from settings import Settings
from ship import Ship
from math import floor
from bullet import Bullet



class Main:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            
        pygame.display.set_caption('Alien Invasion')
        self.clock = pygame.time.Clock()
        self.ship = Ship(self.screen)
        self.bullets = pygame.sprite.Group()
        

        

        # Font for FPS
        self.font = pygame.font.SysFont("Arial", 24)

    def run_game(self):
        #x =100
        #y=100
       
        while True:
            self.check_event()
            self.render()
            self.ship.update()
            self.bullets.update()
            for bullet in self.bullets.copy():
                if bullet.rect.top <= 50:
                    self.bullets.remove(bullet)

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

                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()

                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True

                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

                elif event.key == pygame.K_UP:
                    self.ship.moving_up = True

                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True

                elif event.key == pygame.K_SPACE:
                    self.create_bullet()
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                    
                elif event.key == pygame.K_UP:
                    self.ship.moving_up = False

                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False

    def create_bullet(self):       
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
      
        
    def render(self):
            self.screen.fill(self.settings.bg_color)
            self.render_fps(self.screen, self.clock, self.font)

            
            #pygame.draw.rect(self.screen, (72, 61, 139), (100,200,200,400))
            #x+=.1
            #y+=.2
            self.ship.blitme()

            for bullet in self.bullets.sprites():
             bullet.draw_bullet()

            pygame.display.flip()
            self.clock.tick()        

    def render_fps(self,screen, clock, font):
        fps = int(clock.get_fps())
        fps_text = font.render(f"fps_rate: {fps}", True, (255, 0, 0))
        screen.blit(fps_text, (10, 10))  # Top-left corner



main = Main()
main.run_game()