
import pygame
from pygame.sprite import Sprite 
import random 
from Ennemy import Ennemy

class EnnemyGroup(pygame.sprite.Group):
    def __init__(self, score, max_x, levels) -> None:
        super().__init__()
        self.score = score
        self.max_x = max_x

        self.levels = levels
    
    def spawn(self):
        if len(self.sprites()) == 0: 
            
            # find level
            level = self._find_level()
            
            # spawn ennemies
            for _ in range(level["ennemy_quantity"]):
                print("SPAWN ENNEMY !!!")
                width = self.max_x * 0.1
                random_x = random.randrange(0, self.max_x - width)
                random_y = random.randrange( -width * 3,-width)
                ennemy = Ennemy(random_x, random_y, width, width, level["ennemy_life"])
                self.add(ennemy)

    def destroy(self):
        sprites = self.sprites()
        for sprite in sprites:
            sprite.destroy()

    def is_empty(self):
        sprites = self.sprites()
        return len(sprites) == 0

    def _find_level(self): 
        real_level = self.levels[0]
        for level in self.levels:
            if(level["min_score"] <= self.score.score):
                real_level = level

        return real_level