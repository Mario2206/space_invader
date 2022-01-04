import pygame

class Score:
    def __init__(self, default_score = 0):
        self.default_score = default_score
        self.score = default_score
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
    
    def increment(self, value = 1): 
        self.score += value
    
    def clear(self):
        self.score = self.default_score

    def update(self):
        self.text_surface = self.font.render(str(self.score), False, (255,255,255))
        self.width, _ = self.text_surface.get_size()
    
    def draw(self, screen, win_x):
        MARGIN = 10
        screen.blit(self.text_surface, (win_x - self.width - MARGIN, 10))