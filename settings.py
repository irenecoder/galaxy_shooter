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
        self.screen_height = 800
        self.bg_color =(6,0,4)
        #ship settings
        self.ship_speed_factor= 1
        #alien settings
        self.alien_speed_factor = 1
        #self.fleet_drop_speed = 10
        #fleet direction of one represents right, -1 represents left
       # self.fleet_direction = 1.5
        

