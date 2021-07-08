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
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        #start each alien at the top left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien's exact position
        self.x = float(self.rect.x)


    def blitme(self):
        #draw the alien at its current position
        self.screen.blit(self.image, self.rect)