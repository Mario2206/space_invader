import pygame


class LifeGroup: 
    def __init__(self, life_number, width, height) -> None:
        self.life_number = life_number
        self.default_life_number = life_number
        self.life_group = pygame.sprite.Group()
        self.width = width 
        self.height = height
        self._load_life()

    def draw(self, screen):
        self.life_group.draw(screen)
    

    def remove(self) : 
        list = self.life_group.sprites()
        if self.life_number > 0:
            self.life_group.remove(list[self.life_number - 1])
            self.life_number-= 1
    
    def reset(self):
        self.life_number = self.default_life_number
        self._load_life()

    def _load_life(self) :
        for life_index in range(self.life_number): 
            # configure life item
            MARGIN = 10
            life = pygame.sprite.Sprite()
            life.image = pygame.image.load("assets/player.png")
            life.image = pygame.transform.scale(life.image, (self.width, self.height))
            life.rect = life.image.get_rect()
            life.rect.x = (life_index * self.width) + MARGIN
            life.rect.y = MARGIN

            self.life_group.add(life)