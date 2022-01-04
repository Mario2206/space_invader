import pygame
from GameManager import GameManager

    

module_charge = pygame.init()
clock = pygame.time.Clock()

print(module_charge)

# Game settings
# screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen = pygame.display.set_mode([800, 800])
pygame.display.set_caption("Space Invader 3000")

loop = True

# Screen settings
win_x, win_y = screen.get_size()

game_manager = GameManager(win_x, win_y)

while loop :
    screen.fill((0,0,0))

    for event in pygame.event.get(): 

        game_manager.onEvents(event)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                loop = False 
        if event.type == pygame.QUIT :
            loop = False 
    
    game_manager.update(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
