import pygame
from settings import Settings
from ship import Ship
from math import floor
from bullet import Bullet
from alien import Alien




class Main:
    def __init__(self):
        #pygame is a wrapper for SDL
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(size=(self.settings.width, self.settings.height))
            
        pygame.display.set_caption('Alien Invasion')
        self.clock = pygame.time.Clock()
        #create a ship
        self.ship = Ship(self.screen)

        #creatre a group of bullets
        self.bullets = pygame.sprite.Group()
        #creatre a group of aliens
        self.aliens =  pygame.sprite.Group()
        self.create_fleet()
      
        

        

        # Font for FPS
        self.font = pygame.font.SysFont("Arial", 24)

    def run_game(self):
        #x =100
        #y=100
        
        while True:
            self.check_event()
            self.render()
            self.ship.update()
            self.update_bullets()
            self.aliens.update()
            self.check_fleet_edges()
            #self.screen.fill(self.settings.bg_color)
            #self.render_fps(self.screen, self.clock, self.font)
            #self.ship.blitme()
            #pygame.draw.rect(self.screen, (72, 61, 139), (100,200,200,400))
            #x+=.1
            #y+=.2
            
            #pygame.display.flip()
            self.clock.tick(60)

    def update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.top <= 0:
                self.bullets.remove(bullet)
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)       
        if len(self.aliens) == 0:
            self.create_fleet()

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
        if len(self.bullets) < self.settings.bullet_limit:
         new_bullet = Bullet(self)
         self.bullets.add(new_bullet)

    def create_fleet(self):
        alien = Alien(self)
       #calculating the number of aliens per row
        alien_width = alien.rect.width
        available_space_x = self.settings.width - (alien_width)
        number_of_aliens_x = available_space_x // (2 * alien_width)

         #calculating the number of rows
        alien_height = alien.rect.height
        available_space_y = self.settings.height - self.settings.height //2
        number_of_rows = available_space_y // (2*alien_height)

        for i in range(number_of_aliens_x):
            for j in range(number_of_rows):
             self.create_alien(i,j)
           
    def create_alien(self,ind,row):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + (2*alien_width*ind)
        alien.rect.x = alien.x
        

        alien_height = alien.rect.height
        alien.y = alien_height + (2*alien_height*row)
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def check_fleet_edges(self):
         if self.aliens:
          for alien in self.aliens.sprites():
             if alien.check_edges():
                 self.change_alien_direction()
                 break
                 

    def change_alien_direction(self):
        for alien in self.aliens.sprites():
             alien.rect.y += self.settings.alien_drop_speed
        self.settings.alien_direction *= -1 

    def render(self):
            self.screen.fill(self.settings.bg_color)
            self.render_fps(self.screen, self.clock, self.font)

            
            #pygame.draw.rect(self.screen, (72, 61, 139), (100,200,200,400))
            #x+=.1
            #y+=.2
            self.ship.blitme()

            for bullet in self.bullets.sprites():
             bullet.draw_bullet()

            self.aliens.draw(self.screen)

            pygame.display.flip()
            self.clock.tick()        

    def render_fps(self,screen, clock, font):
        fps = int(clock.get_fps())
        fps_text = font.render(f"fps_rate: {fps}", True, (255, 0, 0))
        screen.blit(fps_text, (10, 10))  # Top-left corner



main = Main()
main.run_game()