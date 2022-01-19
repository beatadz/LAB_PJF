import pygame

class Button(object):
    def __init__(self, text, position, font, text_color, text_size, image, scale, screen):
        self.text = text
        self.x, self.y = position
        self.font = font
        self.text_color = text_color
        self.text_size = text_size
        self.width = image.get_width()
        self.height = image.get_height()
        self.scale = scale
        self.image = pygame.transform.scale(image, (int(self.width * self.scale), int(self.height * scale)))
        self.clicked = False
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def create_button(self):
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        # draw button on screen
        self.screen.blit(self.image, (self.x, self.y))
        # add text
        font = pygame.font.SysFont(self.font, self.text_size)
        button_text = font.render(self.text, True, self.text_color)
        text_width, text_height = font.size(self.text)
        self.screen.blit(button_text, (self.x + self.width/2 - text_width/2, self.y + self.height/2 - text_height/2))

    def click_check(self):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()
        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action