import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, image_path, width, height) -> None:
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0