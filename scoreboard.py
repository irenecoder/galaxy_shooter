import pygame.font


class Scoreboard():
    """a class to report scoring information"""
    def __init__(self,al_settings,screen,stats):
        #initialize scorekeeping attributes
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.al_settings = al_settings
        self.stats = stats

        #font settings for scoring information
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        #prepare the initial score image
        self.prep_score()

    def prep_score(self):
        #turn the score into a rendered message
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.al_settings.bg_color)

        #display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right -20
        self.score_rect.top = 20

    def show_score(self):
        #draw score to the screen
        self.screen.blit(self.score_image,self.score_rect)

