class GameStats():
    #track statistics for alien invasion
    def __init__(self,al_settings):
        #initialize statistics
        self.al_settings = al_settings
        self.reset_stats()
        #start alien invasion in an inactive state
        self.game_active = False
        #high score should never be reset
        self.high_score = 0

    def reset_stats(self):
        #initialize the statistics that can change during the game
        self.ships_left = self.al_settings.ship_limit
        self.score = 0
        self.level = 1


