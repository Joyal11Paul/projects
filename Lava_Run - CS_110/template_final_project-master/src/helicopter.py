import pygame

class Helicopter(pygame.sprite.Sprite):
    def __init__(self):
        '''
        Initializes helicopter object
        args: None
        return: None
        '''
        super().__init__()
        self.image = pygame.image.load("assets/helicopter.jpg")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = [900, 100]