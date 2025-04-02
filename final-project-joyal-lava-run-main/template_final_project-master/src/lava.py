import pygame

class Lava(pygame.sprite.Sprite):
    def __init__(self):
        '''
        Initializes lava object
        args: None
        return: None
        '''
        super().__init__()
        self.image = pygame.image.load("assets/lava.png")
        self.image = pygame.transform.scale(self.image, (1000, 2000))
        self.rect = self.image.get_rect()
        self.rect.center = [500, 1750]
    
    def moving(self):
        '''
        Lava moves upward 
        args: None
        return: None
        '''
        self.rect.y -= 1.5