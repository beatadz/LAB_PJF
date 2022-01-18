import pygame

class Score(object):
    def __init__(self, high_score, screen, board_height, board_width):
        self.game_score = 0
        self.high_score = high_score
        self.points = 10
        self.bonus = 0
        self.screen = screen
        self.board_height = board_height
        self.board_width = board_width

    def display_score(self, font_color, text_size, x, y):
        text = "SCORE: "
        add = str(self.game_score)
        text = text + add
        font = pygame.font.SysFont('arial',  text_size)
        score_text = font.render(text, True, font_color)
        self.screen.blit(score_text, (x, y))
