import pygame as pg
from settings import HEIGHT

COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')


class LiteControlButton:

    def __init__(self, x, y, w, h):
        self.rect = pg.Rect(x, y, w, h)
        self.R = 0
        self.G = 255
        self.B = 0
        self.button_y = 20
        self.x = x
        self.y = y
        self.color = COLOR_INACTIVE
        self.active = False
        self.aria = pg.Surface((w, h))

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
                self.color = COLOR_ACTIVE
                self.button_y = event.pos[-1] + (self.y - HEIGHT)
                self.R = self.button_y
                self.G = 225 - self.R
                print(self.button_y)
                print(self.G, self.R)
            else:
                self.active = False
                self.color = COLOR_INACTIVE
                print('inactive')

    def draw(self, screen):
        self.aria.fill((self.get_lite_value()))
        pg.draw.rect(screen, self.color, self.rect, 5)
        pg.draw.circle(self.aria, (self.R, self.G, self.B), (self.rect.w // 2, self.button_y), (self.rect.w // 2), 20)
        screen.blit(self.aria, (self.x, self.y))

    def get_lite_value(self):
        return self.G, self.G, self.G
