import sys
import pygame
from bullet import Bullet


def check_keydown(event,al_settings,screen,ship,bullets):
    """respond to key presses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #create a new bullet and add it to the bullets group
        new_bullet = Bullet(al_settings,screen,ship)
        bullets.add(new_bullet)

def check_keyup(event,ship):
    """respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_event(al_settings,screen,ship,bullets):
    """respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event,al_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup(event,ship)
        


def update_screen(al_settings,screen,ship,bullets):
    #update images on the screen and flip on the new screen
     #redraw the screen during each pass through the loop
        screen.fill(al_settings.bg_color)
                #make most recently drawn screen visible 
        # redraw all bullets behind ship and aliens
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        
        ship.blitme()

        #make most recently drawn screen visible 
        pygame.display.flip()
        



