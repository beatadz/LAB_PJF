import pygame

class Score(object):
    def __init__(self, lines, screen, board_height, board_width):
        self.game_score = 0
        self.lines = lines
        self.points = 10
        self.bonus = 0
        self.screen = screen
        self.board_height = board_height
        self.board_width = board_width

    def display_score(self, font_color, text_size, x, y):
        text = "SCORE: "
        add = str(self.game_score)
        font = pygame.font.SysFont('arial', text_size)
        text_width, text_height = font.size(add)
        text = text + add
        score_text = font.render(text, True, font_color)
        self.screen.blit(score_text, (x - text_width/2, y))

        text = "LINES: "
        add = str(self.lines)
        text_width, text_height = font.size(add)
        text = text + add
        lines_text = font.render(text, True, font_color)
        self.screen.blit(lines_text, (x - text_width/2, y + text_size + 10))