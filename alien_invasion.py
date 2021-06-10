import sys

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #initialize game and create a screen object
    pygame.init()
    al_settings = Settings()
    screen = pygame.display.set_mode((al_settings.screen_width,al_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship=Ship(screen)
    #set background color
    # bg_color = (230,20,200)

    #start the main loop for the game
    while True:
        #watch for keyboard and mouse events
        gf.check_events(ship)
        """for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() """

        gf.update_screen(al_settings,screen,ship)
        
        

run_game()