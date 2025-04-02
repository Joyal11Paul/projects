import pygame


class Enemies(pygame.sprite.Sprite):
    def __init__(self, y=510):
        '''
        Initializes ghost enemy object
        args: y (y-cord)
        return: None
        '''
        super().__init__()
        self.image = pygame.image.load("assets/enemy.png")   
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.x = 800
        self.y = y
        self.rect.center = [800, self.y]
        self.speed = 2          
        
    def moving(self):
        '''
        Moves back and forth along the platform
        args: None
        return: None
        '''
        if 850 >= self.rect.x >= 700:
            self.rect.x -= self.speed
        else:
            self.speed *= -1
            self.rect.x -= self.speed 
        
    
