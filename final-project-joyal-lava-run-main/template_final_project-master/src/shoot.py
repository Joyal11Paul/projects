import pygame

class Shoot(pygame.sprite.Sprite):
    def __init__(self):
        '''
        Initializes shoot object
        args: None
        return: None
        '''
        super().__init__()
        self.image = pygame.image.load("assets/cannon_ball.jpg")   # Puts image on scree (dont reuse variable names)
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = [50, 250]
        self.speed = 3
        
    def update(self):
        '''
        Updates shot speed
        args: None
        return: None
        '''
        self.rect.x += self.speed
          