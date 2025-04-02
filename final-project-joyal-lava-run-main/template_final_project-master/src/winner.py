import pygame

class Winner(pygame.sprite.Sprite):
    def __init__(self):
        '''
        Initializes winning screen object
        args: None
        return: None
        '''
        super().__init__()
        self.image = pygame.image.load("assets/winner.png")
        self.image = pygame.transform.scale(self.image, (500, 400))
        self.rect = self.image.get_rect()
        self.rect.center = [500, 400]