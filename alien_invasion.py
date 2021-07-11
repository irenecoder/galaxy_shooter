import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from bullet import Bullet


def run_game():
    #initialize game and create a screen object
    pygame.init()
    al_settings = Settings()
    screen = pygame.display.set_mode((al_settings.screen_width,al_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship=Ship(al_settings,screen)
    #make a group to store bullets
    bullets = Group()
    aliens = Group()

    #create the group of aliens
    gf.create_fleet(al_settings,screen,aliens)
    #set background color
    # bg_color = (230,20,200)

    #make an alien
    alien = Alien(al_settings,screen)

    #start the main loop for the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.K_ESCAPE:
                sys.exit()
            elif event.type== pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    ship.moving_left = True
                if event.key == pygame.K_SPACE:
                    #create a new bullet
                    gf.fire_bullet(al_settings,screen, ship,bullets)
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    ship.moving_left = False




        
        #watch for keyboard and mouse events
        #gf.check_event(al_settings,screen,ship,bullets)
        #respond to key presses and mouse events
        ship.update()
        gf.update_bullets(bullets)
       
        gf.update_screen(al_settings,screen,ship,aliens,bullets)
        
        

run_game()