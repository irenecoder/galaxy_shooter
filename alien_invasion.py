import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    #initialize game and create a screen object
    pygame.init()
    al_settings = Settings()
    screen = pygame.display.set_mode((al_settings.screen_width,al_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship=Ship(al_settings,screen)
    #make a group to store bullets
    bullets = Group()
    #set background color
    # bg_color = (230,20,200)

    #start the main loop for the game
    while True:
      
        #watch for keyboard and mouse events
        gf.check_event(al_settings,screen,ship,bullets)
        #respond to key presses and mouse events
        ship.update()
        bullets.update()

        gf.update_screen(al_settings,screen,ship,bullets)
        
        

run_game()