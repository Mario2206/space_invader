import pygame
from Ennemy import Ennemy
from EnnemyGroup import EnnemyGroup
from GameOver import GameOver
from LifeGroup import LifeGroup
from Ship import Ship
from Score import Score

class GameManager: 
    def __init__(self, win_x, win_y) -> None:
        # Add game items
        self.player = Ship(win_x / 2, win_y * 0.85, win_x * 0.1, win_y * 0.1)
        self.score = Score(0)
        self.life = LifeGroup(3, win_x * 0.06, win_x * 0.06)

        # Add background
        self.background = pygame.image.load("assets/background.jpg")
        self.background = pygame.transform.scale(self.background, (win_x, win_y))

        # Add gameover
        self.game_over_scene = GameOver(self.score, self.life)

        # Add music 
        self.music = pygame.mixer.music.load('assets/sounds/music.mp3')
        pygame.mixer.music.play(-1)

        # Get game settings
        self.win_x = win_x
        self.win_y = win_y
        self.levels = [
            {'min_score': 0, 'ennemy_quantity': 1, 'ennemy_life': 1},
            {'min_score': 1, 'ennemy_quantity': 5, 'ennemy_life': 1},
            {'min_score': 10, 'ennemy_quantity': 8, 'ennemy_life': 2},
            {'min_score': 20, 'ennemy_quantity': 14, 'ennemy_life': 2},
            {'min_score': 34, 'ennemy_quantity': 15, 'ennemy_life': 3},
            {'min_score': 50, 'ennemy_quantity': 40, 'ennemy_life': 3},
        ]

        # Create groups
        self.player_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.ennemy_group = EnnemyGroup(self.score, self.win_x, self.levels)

        self.player_group.add(self.player)

    def update(self, screen):
        # Draw background
        screen.blit(self.background, (0,0))

        if self.life.life_number == 0:
            self.game_over(screen)
        else: 
            # Update game values
            self.player.update()

            self.manage_bullets()
            self.bullet_group.update()
            
            self.ennemy_group.spawn()
            self.manage_ennemies()
            self.ennemy_group.update()

            self.score.update()
            self.player.checkBorderCollision([0, self.win_x])
            

            # Draw game
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
        
        if self.game_over_scene.button.is_clicked(event):
            self.restart_game()

    def manage_ennemies(self):
        for ennemy in self.ennemy_group.sprites():
            bullet_collision = pygame.sprite.spritecollideany(ennemy, self.bullet_group)

            # Filter ennemies
            if ennemy.can_be_removed():
                print("ENNEMY REMOVED FROM GAME")
                self.ennemy_group.remove(ennemy)

            if bullet_collision and not ennemy.is_destroyed:
                ennemy.damage()
                self.bullet_group.remove(bullet_collision)
                if ennemy.is_destroyed :
                    print("ENNEMY KILLED")
                    self.score.increment()
            
            if ennemy.rect.y + ennemy.height >= self.player.rect.y and not ennemy.is_destroyed :
                self.life.remove()
                ennemy.destroy()

    def manage_bullets(self) : 
        for bullet in self.bullet_group.sprites() :
            if bullet.check_if_bullet_is_out() :
                self.bullet_group.remove(bullet)


    def game_over(self, screen):

        if not self.ennemy_group.is_empty():
            self.manage_ennemies()
            self.ennemy_group.destroy()
            self.ennemy_group.update()
            self.ennemy_group.draw(screen)
            return
        else:
            self.game_over_scene.update()
            self.game_over_scene.draw(screen, self.win_x, self.win_y)
            pygame.mixer.music.pause()
    
        # self.ennemy_group.empty()
        
        
    def restart_game(self):
        self.score.clear()
        self.life.reset()
        pygame.mixer.music.play(-1)

        print("restart game")