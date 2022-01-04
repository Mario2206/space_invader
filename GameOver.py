import pygame

class GameOver:
    def __init__(self, score, player_life) -> None:
        self.score = score 
        self.player_life = player_life
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.surfaces = []

    def update(self):
        self.surfaces = []
        title = self.font.render("Game Over !!!",  False, (255,255,255))
        score = self.font.render(f"Score: {self.score.score}",  False, (255,255,255))
        life = self.font.render(f"Life: {self.player_life.life_number}",  False, (255,255,255))

        self.surfaces.append(title)
        self.surfaces.append(score)
        self.surfaces.append(life)
    
    def draw(self, screen, win_x, win_y):
        total_height = 0
        items = []
        for surface in self.surfaces:
            width, height = surface.get_size()
            x = (win_x / 2) - (width / 2)
            y = (win_y / 2) - (height / 2) + total_height
            total_height += height
            items.append([surface, (x, y)])
            # screen.blit(surface, (x, y))

        for item in items: 
            x, y = item[1]
            y -= total_height / 2
            screen.blit(item[0], (x, y) )