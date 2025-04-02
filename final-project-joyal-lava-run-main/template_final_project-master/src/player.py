import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        '''
        Initializes player object
        args: None
        return: None
        '''
        super().__init__()
        self.p_jumping = False
        self.image = pygame.image.load("assets/peter_griffin.png")   # Puts image on screen (dont reuse variable names)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = [200, 620]          # Centers it at [200, 660]
        self.speed_side = 10
        self.speed_down = 3
        self.is_bouncing = True
        
    def move_right(self):
        '''
        Moves right when "D" is pressed 
        args: None
        return: None
        '''
        self.rect.x += self.speed_side
    
    def move_left(self):
        '''
        Moves left when "A" key is pressed 
        args: None
        return: None
        '''
        self.rect.x -= self.speed_side
    
    def down(self):
        '''
        Moves down when "S" key is pressed
        args: None
        return: None
        '''
        self.rect.y += self.speed_side
    
    def jumping(self):
        '''
        Moves up 1 jump when "W" key is pressed
        args: None
        return: None
        '''
        self.rect.y -= 90
    
    def falling(self):
        '''
        Makes sure the player is falling
        args: None
        return: None
        '''
        self.rect.y += self.speed_down
    