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


def get_number_aliens_x(al_settings,alien_width):
    #determine the number of aliens that fit in a row
    available_space_x = al_settings.screen_width - 2* alien_width
    number_aliens_x = int(available_space_x / (2* alien_width))
    return number_aliens_x

def get_number_rows(al_settings,ship_height,alien_height):
    #determine the number of rows of aliens that fit on the screen
    available_space_y = (al_settings.screen_height - (2* alien_height)- ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(al_settings,screen,aliens,alien_number,row_number):
    #create an alien and place it in the row
    alien = Alien(al_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height +2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(al_settings,screen,ship,aliens):
    """Create a full fleet of aliens"""
    #create an alien and find the number of aliens in a row
    #spacing between each alien is equal to one alien width
    alien = Alien(al_settings,screen)
    number_aliens_x = get_number_aliens_x(al_settings,alien.rect.width)  
    number_rows = get_number_rows(al_settings,ship.rect.height,alien.rect.height)

    #create the fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(al_settings,screen,aliens,alien_number,row_number)

        



