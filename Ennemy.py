import pygame 

class Ennemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, life = 1 ) -> None:
        super().__init__()
        self.width = width 
        self.height = height
        self.image = pygame.image.load("assets/ennemy.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
        self.speed = 1
        self.is_destroyed = False 
        
        self.is_animating = False
        self.animation_sprite_index = 0
        self.destroy_sound = pygame.mixer.Sound("assets/sounds/explosion.wav")

        # Load animation sprites
        self.destroy_sprites = []
        for sprite_index in range(24) :
            self.destroy_sprites.append(pygame.image.load(f"assets/animations/explosion/explosion_{sprite_index + 1}.png"))
        
        self.life = life
    
    def update(self):
        if not self.is_destroyed :
            self.rect.y += self.speed

        if self.is_animating and self.is_destroyed: 
          
            self.animation_sprite_index += 0.4

            if int(self.animation_sprite_index) >= len(self.destroy_sprites) :
                self.is_animating = False
            else :
                self.image = self.destroy_sprites[int(self.animation_sprite_index)]

    def damage(self):
        self.life-= 1
        if self.life <= 0:
            self.destroy()
        else: 
            self.destroy_sound.play()

    def destroy(self):
        if not self.is_destroyed:  
            self.destroy_sound.play()
            self.is_destroyed = True 
            self.is_animating = True
    
    def can_be_removed(self):
        return self.is_destroyed and not self.is_animating
