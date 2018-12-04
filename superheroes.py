# Background images courtesy of Author: ramses2099 from OpenGameArt.org https://opengameart.org/content/background-2

# imports
import pygame
import os
from Player import Player

# initialization
pygame.init()
pygame.display.set_caption('Blue Team - Super Heroes')
fps_clock = pygame.time.Clock()
FPS = 30    # 30 frames per second

# Set up background
WIDTH, HEIGHT = 900, 550
game_surface = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load(os.path.join('art', 'backgrounds', 'forest.png')).convert()
background_vertical_offset = HEIGHT - background.get_height()

# Instantiate the players and player list
catboy = Player("catboy", "Catboy", WIDTH//2 + 32, HEIGHT - 32 - 20, 32, 32, 1)
hoppy = Player("hoppy", "Hoppy", WIDTH//2 - 32, HEIGHT - 32 - 20, 32, 32, 2)
players = [catboy, hoppy]

def redrawGameWindow():
    game_surface.blit(background, (0,background_vertical_offset))
    for player in players: 
        player.draw(game_surface)
    
def run_game():
    redrawGameWindow()
    pygame.display.update()
    run = True
    while run:
        fps_clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False 

        # capture key inputs
        pressed_keys = pygame.key.get_pressed()
        
        # move character according to key inputs
        for player in players: 
            player.move(pressed_keys, game_surface)
        
        redrawGameWindow()
        pygame.display.update()
    
    # exit game
    pygame.quit()

if __name__ == '__main__':
    run_game()