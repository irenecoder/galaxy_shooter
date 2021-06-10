import sys
import pygame

def check_events(ship):
    """respond to key presses and mouse events""" 
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    #shift ship to the right
                    ship.rect.centerx +=1
                elif event.type==pygame.K_RCTRL:
                    ship.rect.centerx -=1

            # elif event.type == pygame.KEYUP:

def update_screen(al_settings,screen,ship):
    #update images on the screen and flip on the new screen
     #redraw the screen during each pass through the loop
        screen.fill(al_settings.bg_color)
                #make most recently drawn screen visible 
        ship.blitme()
        pygame.display.flip()


