import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height) -> None:
        super().__init__()
        self.image = pygame.image.load("assets/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        self.width = width 
        self.height = height
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.speed = 6
    
    def update(self):
        self.rect.y -= self.speed
    
    def check_if_bullet_is_out(self):
        if self.rect.y + self.height < 0 :
            return True
        
        return False