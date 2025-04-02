import pygame

class Collision_Plat:
    def __init__(self, x = 200, y = 700):
        '''
        Initializes collision plat object
        args: x, y (x-cord, y-cord)
        return: None
        '''
        self.x = x
        self.y = y - 12.5
        self.rect = pygame.rect.Rect(self.x, self.y, 190, 1)
        self.rect.center = [self.x, self.y]
        
    