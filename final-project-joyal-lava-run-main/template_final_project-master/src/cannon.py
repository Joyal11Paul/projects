import pygame

class Cannon(pygame.sprite.Sprite):
    def __init__(self):
        '''
        Initializes ghost enemy object
        args: None
        return: None
        '''
        super().__init__()
        self.image = pygame.image.load("assets/cannon.png")   # Puts image on scree (dont reuse variable names)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = [25, 250]          
        
        