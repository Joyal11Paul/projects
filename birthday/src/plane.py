import pygame

class Plane(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/plane.png")
        self.image = pygame.transform.scale(self.image, (300, 200))    #(1000, 500)
        self.rect = self.image.get_rect()
        self.rect.x = -200
        self.rect.y = 400
        
        
    
        
        