import pygame

class Balloons(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/pikachu_balloon_sprite.png")
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.center = [100, 650]
        
    def moving(self):
        self.rect.x += 0.75
        self.rect.y -= 0.75
    
    def balloon_scale(self, scale = 1):
        self.image = pygame.transform.scale_by(self.image, scale)