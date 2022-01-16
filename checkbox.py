import pygame

class Checkbox:
    def __init__(self, screen, x, y, color, text, outline_color, check_color, font_size, font_color, text_offset, font):
        self.screen = screen
        self.x = x
        self.y = y
        self.color = color
        self.text = text
        self.outline_color = outline_color
        self.check_color = check_color
        self.font_size = font_size
        self.font_color = font_color
        self.text_offset = text_offset
        self.font = font
        self.checkbox_size = 15

        # checkbox object
        self.checkbox_obj = pygame.Rect(self.x, self.y, self.checkbox_size, self.checkbox_size)
        self.checkbox_outline = self.checkbox_obj.copy()

        # variables to test the different states of the checkbox
        self.checked = False

    def _draw_button_text(self):
        self.font = pygame.font.SysFont(self.font, self.font_size)
        width, height = self.font.size(self.text)
        self.font_position = (self.x + self.text_offset[0], self.y + 15 / 2 - height / 2 + self.text_offset[1])
        self.screen.blit(self.font.render(self.text, True, self.font_color), self.font_position)

    def render_checkbox(self):
        if self.checked:
            pygame.draw.rect(self.screen, self.color, self.checkbox_obj)
            pygame.draw.rect(self.screen, self.outline_color, self.checkbox_outline, 1)
            pygame.draw.circle(self.screen, self.check_color, (self.x + 6, self.y + 6), 4)

        elif not self.checked:
            pygame.draw.rect(self.screen, self.color, self.checkbox_obj)
            pygame.draw.rect(self.screen, self.outline_color, self.checkbox_outline, 1)
        self._draw_button_text()

    def _update(self, event_object):
        x, y = pygame.mouse.get_pos()
        px, py, w, h = self.checkbox_obj
        if px < x < px + w and py < y < py + w:
            if self.checked:
                self.checked = False
            else:
                self.checked = True

    def update_checkbox(self, event_object):
        if event_object.type == pygame.MOUSEBUTTONDOWN:
            self.click = True
            self._update(event_object)