import pygame

class GameOver(pygame.sprite.Sprite):
    def __init__(self):
        '''
        Initializes game over screen object
        args: None
        return: None
        '''
        super().__init__()
        self.image = pygame.image.load("assets/game_over.png")
        self.image = pygame.transform.scale(self.image, (500, 400))
        self.rect = self.image.get_rect()
        self.rect.center = [500, 400]