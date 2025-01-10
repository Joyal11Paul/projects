import pygame

class Clouds(pygame.sprite.Sprite):
    def __init__(self, x = 0):
        super().__init__()
        self.image = pygame.image.load("assets/clouds_sprite.png")
        self.image = pygame.transform.scale(self.image, (2000, 1000))    #(1000, 500)
        self.rect = self.image.get_rect()
        self.rect.x = x
        
    def cloud_scale(self, scale = 1):
        self.image = pygame.transform.scale_by(self.image, scale)
    
        
        