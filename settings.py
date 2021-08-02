class Settings():
    #a class to store all settings for alien invasion
    def __init__(self):
        #bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255,255,255
        self.bullets_allowed = 3
        #initialize the game static settings
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color =(6,0,4)
        #ship settings
        self.ship_speed_factor= 1
        self.ship_limit = 3
        #alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #how quickly the game speeds up
        self.speed_up_scale = 1.1
        #how quickly the alien point value increases
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        #fleet direction of one represents right, -1 represents left
        self.fleet_direction = 1

    def initialize_dynamic_settings(self):
        #initialize the settings that change throughout the game
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1.2

        #fleet direction of 1 represents right, -1 represents left
        self.fleet_direction = 1.5
        #scoring
        self.alien_points = 40

    def increase_speed(self):
        """increase speed settings and alien point values"""
        self.ship_speed_factor *= self.speed_up_scale
        self.bullet_speed_factor *= self.speed_up_scale
        self.alien_speed_factor *= self.speed_up_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        

         

