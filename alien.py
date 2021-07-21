import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #a class to represent a single alien in a fleet

    def __init__(self,al_settings,screen):
        #initialize the alien and set its starting position
        super(Alien,self).__init__()
        self.screen = screen
        self.al_settings = al_settings

        #load the alien image and set the rect attribute
        self.image = pygame.image.load("images/aliship.bmp")
        self.rect = self.image.get_rect()

        #start each alien at the top left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien's exact position
        self.x = float(self.rect.x)


    def blitme(self):
        #draw the alien at its current position
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        #return true if alien is at edge of the screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <=0:
            return True

    def update(self):
        #move the alien to the right or left

        self.x += (self.al_settings.alien_speed_factor * self.al_settings.fleet_direction)
        self.rect.x = self.x
