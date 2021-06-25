import  pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #a class to manage all bullets fired from the ship
    def __init__(self,al_settings,screen,ship):
        """create a bullet object at the ship's current position"""
        super(Bullet,self). __init__()
        self.screen = screen

        #create a bullet at point 0,0 and then correct the position
        self.rect = pygame.Rect(0, 0,al_settings.bullet_width,al_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #store the ship position as a decimal value
        self.y = float(self.rect.y)

        self.color = al_settings.bullet_color
        self.speed_factor = al_settings.bullet_speed_factor

    def update(self):
        #move the bullet up the screen
        #update the decimal position of the bullet
        self.y -= self.speed_factor
        #update the rect position
        self.rect.y = self.y
    def draw_bullet(self):
        #draw the bullet
        pygame.draw.rect(self.screen,self.color,self.rect)

