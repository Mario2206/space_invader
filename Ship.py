import pygame

from Bullet import Bullet

class Ship(pygame.sprite.Sprite):
    def __init__(self, x,y, width, height ) -> None:
        super().__init__()
        self.dir = 0
        self.height = height
        self.width = width
        self.speed = 5

        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect.x = x
        self.rect.y = y

        self.shoot_sound = pygame.mixer.Sound("assets/sounds/shoot.mp3")
    
    def update(self):
        self.rect.x +=  (1 * self.dir * self.speed)

    def onEvents(self, event): 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                self.dir = -1
            
            if event.key == pygame.K_d:
                self.dir = 1
            
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q or event.key == pygame.K_d: 
                self.dir = 0
            
    def shoot(self, width, height):
        bullet = Bullet(self.rect.x + (self.width / 2), self.rect.y - height, width, height)
        self.shoot_sound.play()
        return bullet

    def checkBorderCollision(self, limits_x) :
        if self.rect.x + self.width >= limits_x[1] : 
            self.dir = -1
        if self.rect.x <= limits_x[0] :
            self.dir = 1