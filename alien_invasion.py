import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
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

    #make the play button
    play_button = Button(al_settings,screen,"Play")
    #display an instance to store statistics and create a scoreboard
    stats = GameStats(al_settings)
    sb = Scoreboard(al_settings,screen,stats)

    ship=Ship(al_settings,screen)
    #make a group to store bullets
    bullets = Group()
    aliens = Group()

    #create the group of aliens
    gf.create_fleet(al_settings,screen,ship,aliens)
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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                check_play_button(al_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y)

        def check_play_button(al_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y):
            #start a new game when the player hits play
            button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
            if button_clicked and not stats.game_active:
                #reset the game settings
                al_settings.initialize_dynamic_settings()
                #hide the mouse cursor
                pygame.mouse.set_visible(False)
                #reset game statistics
                stats.reset_stats()
                stats.game_active = True

                #empty the list of aliens and bullets
                aliens.empty()
                bullets.empty()

                #create a new fleet and center the fleet
                gf.create_fleet(al_settings, screen, ship, aliens)
                ship.center_ship()




        
        #watch for keyboard and mouse events
        #gf.check_event(al_settings,screen,ship,bullets)
        #respond to key presses and mouse events
        if stats.game_active:

            ship.update()
            gf.update_bullets(al_settings,screen,ship,aliens,bullets)
            gf.update_aliens(al_settings,stats,screen,ship,aliens,bullets)

        gf.update_screen(al_settings,screen,stats,sb,ship,aliens,bullets,play_button)
        
        
        

run_game()