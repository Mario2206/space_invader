import pygame 

class Ennemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height ) -> None:
        super().__init__()
        self.width = width 
        self.height = height
        self.image = pygame.image.load("assets/ennemy.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
        self.speed = 1
    
    def update(self):
        self.rect.y += self.speed
