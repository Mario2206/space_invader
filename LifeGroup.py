import pygame


class LifeGroup: 
    def __init__(self, life_number, width, height) -> None:
        self.life_number = life_number
        
        self.life_group = pygame.sprite.Group()

        for life_index in range(self.life_number): 
            # configure life item
            MARGIN = 10
            life = pygame.sprite.Sprite()
            life.image = pygame.image.load("assets/player.png")
            life.image = pygame.transform.scale(life.image, (width, height))
            life.rect = life.image.get_rect()
            life.rect.x = (life_index * width) + MARGIN
            life.rect.y = MARGIN

            self.life_group.add(life)

    def draw(self, screen):
        self.life_group.draw(screen)
    
    def remove(self) : 
        list = self.life_group.sprites()
        list_length = len(list)
        self.life_group.remove(list[list_length - 1])