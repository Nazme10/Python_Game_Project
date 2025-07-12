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

        # Font for FPS
        self.font = pygame.font.SysFont("Arial", 24)

    def run_game(self):
        x =100
        y=100
       
        while True:
            events = pygame.event.get()
            print(events)
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            self.screen.fill(self.settings.bg_color)
            self.render_fps(self.screen, self.clock, self.font)
            self.ship.blitme()
            pygame.draw.rect(self.screen, (72, 61, 139), (x,y,200,400))
            x+=.1
            y+=.2
            
            pygame.display.flip()
            self.clock.tick()

    def render_fps(self,screen, clock, font):
        fps = int(clock.get_fps())
        fps_text = font.render(f"fps_rate: {fps}", True, (255, 0, 0))
        screen.blit(fps_text, (10, 10))  # Top-left corner



main = Main()
main.run_game()