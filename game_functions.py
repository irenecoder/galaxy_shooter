import sys
from time import sleep
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
        
def update_bullets(al_settings,screen,stats,sb,ship,aliens,bullets):

    """update position of bullets and get rid of old bullets"""
    #update bullet positions
    bullets.update()
    #Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:         
            bullets.remove(bullet)
            #print(len(bullets))
    check_bullet_alien_collision(al_settings,screen,stats,sb,ship,aliens,bullets)

def check_bullet_alien_collision(al_settings,screen,stats,sb,ship,aliens,bullets):

    #check for any bullets that have hit aliens
    #if so get rid of the bullet and the alien
    collisions = pygame.sprite.groupcollide(bullets,aliens,False,True)
    if collisions:
        for aliens in collisions.values():
            stats.score +=al_settings.alien_points* len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)

    if len(aliens) == 0:
        
        #if the entire fleet is destroyed,start a new level
        bullets.empty()
        al_settings.increase_speed()
        #increase level
        stats.level += 1
        sb.prep_level()
        create_fleet(al_settings, screen, ship, aliens)

    #Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:         
            bullets.remove(bullet)
            #print(len(bullets))


def update_screen(al_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    #update images on the screen and flip on the new screen
     #redraw the screen during each pass through the loop
        screen.fill(al_settings.bg_color)
                #make most recently drawn screen visible 
        # redraw all bullets behind ship and aliens
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        
        ship.blitme()
        aliens.draw(screen)

        #draw the score information
        sb.show_score()
        #draw the play button if the game is inactive
        if not stats.game_active:
            play_button.draw_button()

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

# def change_fleet_direction(al_settings,aliens):
#     """drop the entire fleet and fleet direction"""
#     for alien in aliens.sprites():
#         alien.rect.y += al_settings.fleet_drop_speed
#     al_settings.fleet_direction *= -1

def check_fleet_edges(al_settings,aliens):
    """respond appropriately if any aliens have reached the edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(al_settings,aliens)
            break

def change_fleet_direction(al_settings,aliens):
    #drop the entire fleet and fleet direction
    for alien in aliens.sprites():
        alien.rect.y += al_settings.fleet_drop_speed
    al_settings.fleet_direction *= -1
    #al_settings.fleet_direction *= +1

def ship_hit(al_settings,screen,stats,sb,ship,aliens,bullets):
    #respond to ship being hit by aliens
    if stats.ships_left > 0:

        #decrement ships_left
        stats.ships_left -=1
        #update scoreboard
        sb.prep_ships()

        #empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        #create a new fleet and center the ship
        create_fleet(al_settings, screen, ship, aliens)
        ship.center_ship()

        #pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_bottom_aliens(al_settings,screen,stats,sb,ship,aliens,bullets):
    """check if any aliens have reached the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >=screen_rect.bottom:
            #treat it like ship got hit
            ship_hit(al_settings,screen,stats,sb, ship, aliens, bullets)
            break




def update_aliens(al_settings,screen,stats,sb,ship,aliens,bullets):
    """check if the fleet is at an edge and then update positions of all aliens in the fleet"""
    check_fleet_edges(al_settings,aliens)
    aliens.update()
    #look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(al_settings,screen,stats,sb,ship,aliens,bullets)
        #print("Ship hit!!")

    #look for aliens reaching bottom of the screen
    check_bottom_aliens(al_settings,screen,stats,sb,ship,aliens,bullets)

def check_high_score(stats,sb):
    #check to see if there is a new high score
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

        



