class Settings():
    #a class to store all settings for alien invasion
    def __init__(self):
        #bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255,255,255
        self.bullets_allowed = 3
        #initialize the game settings
        #screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color =(6,0,4)
        #ship settings
        self.ship_speed_factor= 1
        

