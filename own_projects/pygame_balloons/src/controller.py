import pygame, sys
from src.balloons import Balloons
from src.clouds import Clouds

class Controller():
    def __init__(self):    
        pygame.init()
        pygame.event.pump()
        pygame.display.init()
        self.clock = pygame.time.Clock()
        self.width = 1000
        self.height = 800
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Lava Run")
        self.balloon = Balloons()
        self.clouds = Clouds()
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.clouds, self.balloon)
        self.bg_color = (0, 0, 250)
    
    def mainloop(self):
        running = True
        baloon_scale = 1
        count = 0
        x_val_clouds = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        running = False
            
            self.balloon.moving()
            
            if count > 500:
                self.balloon.balloon_scale(scale=baloon_scale)
                self.clouds.cloud_scale(scale=baloon_scale)
                baloon_scale -= 0.005
                count = 0


            pygame.display.flip()
            self.window.fill(self.bg_color)
            self.sprites.update()
            self.sprites.draw(self.window)
            count += 10
            
        
        pygame.quit()
        sys.exit()