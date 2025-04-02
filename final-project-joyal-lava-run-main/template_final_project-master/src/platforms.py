import pygame

class Platforms(pygame.sprite.Sprite):
    def __init__(self, x, y):
        '''
        Initializes platform object
        args: None
        return: None
        '''
        super().__init__()
        self.image = pygame.image.load("assets/platform.png")   
        self.image = pygame.transform.scale(self.image, (200, 25))
        self.rect = self.image.get_rect()
        self.rect = self.rect.scale_by(1, 0.8)
        self.x = x
        self.y = y
        self.rect.center = [self.x, self.y]
        
    def return_point_right(self):
        '''
        Gets the right midpoint of a plat
        args: None
        return: int 
        '''
        self.right = self.x + 100
        self.mid_height = self.y + 3 
        self.my_point = (self.right, self.mid_height)
        return self.my_point
    
    def return_point_left(self):
        '''
        Gets the left midpoint of a plat
        args: None
        return: int 
        '''
        self.left = self.x - 100
        self.mid_height = self.y + 3
        self.my_point = (self.left, self.mid_height)
        return self.my_point
    
  