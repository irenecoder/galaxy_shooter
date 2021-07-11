import sys
import pygame
from bullet import Bullet
from alien import Alien


"""def check_keydown(event,al_settings,screen,ship,bullets):
    respond to key presses
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #create a new bullet and add it to the bullets group
        new_bullet = Bullet(al_settings,screen,ship)
        bullets.add(new_bullet)

def check_keyup(event,ship):
    respond to key releases
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_event(al_settings,screen,ship,bullets):
    respond to keypresses and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event,al_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup(event,ship)"""

def fire_bullet(al_settings,screen,ship,bullets):
    """fire a bullet if limit not reached yet"""
    #create a new bullet and add it to the bullets group
    new_bullet = Bullet(al_settings,screen,ship)
    bullets.add(new_bullet)
        
def update_bullets(bullets):
    """update position of bullets and get rid of old bullets"""
    #update bullet positions
    bullets.update()

    #Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:         
            bullets.remove(bullet)
            #print(len(bullets))


def update_screen(al_settings,screen,ship,aliens,bullets):
    #update images on the screen and flip on the new screen
     #redraw the screen during each pass through the loop
        screen.fill(al_settings.bg_color)
                #make most recently drawn screen visible 
        # redraw all bullets behind ship and aliens
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        
        ship.blitme()
        aliens.draw(screen)

        #make most recently drawn screen visible 
        pygame.display.flip()

def create_fleet(al_settings,screen,aliens):
    """Create a full fleet of aliens"""
    #create an alien and find the number of aliens in a row
    #spacing between each alien is equal to one alien width
    alien = Alien(al_settings,screen)
    alien_width = alien.rect.width
    available_space_x = al_settings.screen_width - 2* alien_width
    number_aliens_x = int(available_space_x / (2* alien_width))

    #create first row of aliens
    for alien_number in range(number_aliens_x):
        #Create an alien and place it in a row
        alien = Alien(al_settings,screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
        



