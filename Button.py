import pygame 

class Button:
    def __init__(self, text, x = 0, y = 0) -> None:
        self.text = text
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.button = self.font.render(self.text,  False, (255,255,255))
        self.width, self.height = self.button.get_size()
        self.x = x 
        self.y = y 

    def draw(self, screen):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, (0,0,0), self.rect)
        screen.blit(self.button, (self.x, self.y))

    def is_clicked(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]  and hasattr(self, "rect"):
                if self.rect.collidepoint(x, y):
                    return True

        return False