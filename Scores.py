import pygame.font

class Scores():
    """Output of information about the game"""
    def __init__(self, screen, stats):
        """initialize score"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (148, 0, 211)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()

    def image_score(self):
        """Transformation txt of score into an image"""
        self.score_img = self.font.render(str(self.stats.GunsLeft),True , self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

        self.score_img_enemy = self.font.render(str(self.stats.EnemyLeft), True, self.text_color, (0, 0, 0))
        self.score_rect_enemy = self.score_img_enemy.get_rect()
        self.score_rect_enemy.right = self.screen_rect.right - 40
        self.score_rect_enemy.top = 60

    def show_score(self):
        """Output a score on the screen"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.score_img_enemy, self.score_rect_enemy)