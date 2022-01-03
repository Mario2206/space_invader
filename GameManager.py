import pygame
from Background import Background
from Ennemy import Ennemy
from LifeGroup import LifeGroup
from Ship import Ship
from Score import Score
import random

class GameManager: 
    def __init__(self, win_x, win_y) -> None:
        # Add game items
        self.player = Ship(win_x / 2, win_y * 0.85, win_x * 0.1, win_y * 0.1)
        self.score = Score()
        self.life = LifeGroup(3, win_x * 0.06, win_x * 0.06)
        self.background = pygame.image.load("assets/background.jpg")
        self.background = pygame.transform.scale(self.background, (win_x, win_y))

        # Get game settings
        self.win_x = win_x
        self.win_y = win_y

        # Create groups
        self.player_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.ennemy_group = pygame.sprite.Group()

        self.player_group.add(self.player)

    def update(self, screen):

        # Update game values
        self.player.update()

        self.filter_bullets()
        self.bullet_group.update()
        
        self.spawn_ennemies()
        self.manage_ennemies()
        self.ennemy_group.update()

        self.score.update()
        self.player.checkBorderCollision([0, self.win_x])

        # Draw game
        screen.blit(self.background, (0,0))
        self.player_group.draw(screen)
        self.bullet_group.draw(screen)
        self.ennemy_group.draw(screen)
        self.life.draw(screen)
        self.score.draw(screen, self.win_x)

    def onEvents(self, event): 
        self.player.onEvents(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = self.player.shoot(self.win_x * 0.03, self.win_x * 0.06)
                self.bullet_group.add(bullet)

    def spawn_ennemies(self):
        if len(self.ennemy_group.sprites()) == 0: 
            print("SPAWN ENNEMY !!!")
            width = self.win_x * 0.1
            random_x = random.randrange(0, self.win_x - width )
            ennemy = Ennemy(random_x, -width, width, width)
            self.ennemy_group.add(ennemy)

    def manage_ennemies(self):
        for ennemy in self.ennemy_group.sprites():
            bullet_collision = pygame.sprite.spritecollideany(ennemy, self.bullet_group)
        
            if bullet_collision :
                print("ENNEMY KILLED")
                self.ennemy_group.remove(ennemy)
                self.bullet_group.remove(bullet_collision)
                self.score.increment()
            
            if ennemy.rect.y + ennemy.height >= self.player.rect.y :
                self.life.remove()
                self.ennemy_group.remove(ennemy)

    def filter_bullets(self) : 
        for bullet in self.bullet_group.sprites() :
            if bullet.check_if_bullet_is_out() :
                self.bullet_group.remove(bullet)

