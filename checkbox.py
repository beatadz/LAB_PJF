import pygame

class Checkbox:
    def __init__(self, screen, x, y, color, text, outline_color, check_color, font_size, font_color, text_x, text_y, font_, text_background):
        self.screen = screen
        self.x = x
        self.y = y
        self.color = color
        self.text = text
        self.outline_color = outline_color
        self.check_color = check_color
        self.font_size = font_size
        self.font_color = font_color
        self.text_x = text_x
        self.text_y = text_y
        self.font_ = font_
        self.font = pygame.font.SysFont(self.font_, self.font_size)
        self.text_background = text_background
        self.checkbox_size = 15
        self.time = pygame.time.Clock().tick(1000)
        self.checked = False
        # checkbox object
        self.checkbox_obj = pygame.Rect(self.x, self.y, self.checkbox_size, self.checkbox_size)
        self.checkbox_outline = self.checkbox_obj.copy()

        self.rectangle = pygame.Rect(self.checkbox_obj)

    def draw_button_text(self):
        font_position = (self.x + self.checkbox_size + 10, self.y - 4)
        self.screen.blit(self.font.render(self.text, True, self.font_color, self.text_background), font_position)

    def render_checkbox(self):
        self.time += pygame.time.Clock().tick(1000)

        if self.checked:
            pygame.draw.rect(self.screen, self.color, self.checkbox_obj)
            pygame.draw.rect(self.screen, self.outline_color, self.checkbox_outline, 1)
            pygame.draw.rect(self.screen, self.check_color, (self.x + 1, self.y + 1, self.checkbox_size - 2, self.checkbox_size - 2), 0)
        elif not self.checked:
            pygame.draw.rect(self.screen, self.color, self.checkbox_obj)
            pygame.draw.rect(self.screen, self.outline_color, self.checkbox_outline, 1)

        self.draw_button_text()

    def update_checkbox(self):
        pos = pygame.mouse.get_pos()
        if self.rectangle.collidepoint(pos):
            if self.time/1000.0 > 0.01:
                self.time = 0
                if not self.checked:
                    self.checked = True
                elif self.checked:
                    self.checked = False