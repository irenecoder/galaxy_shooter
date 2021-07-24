import pygame

class Ship():
    def __init__(self,al_settings,screen):
        #initialize the ship and get its initial position
        self.screen=screen
        self.al_settings = al_settings
        #load image and get its rect
        self.image= pygame.image.load("images/rocket1b.bmp")
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #start each new ship at the bottom center
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        #store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

         #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #update the ships position depending on the movement
        #update the ship's center value not the rect
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.rect.centerx += self.al_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center-= self.al_settings.ship_speed_factor

            #update rect object from self.center
            self.rect.centerx = self.center

    def blitme(self):
        #drawing the ship at its current location
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        #center the ship on the screen
        self.center = self.screen_rect.centerx