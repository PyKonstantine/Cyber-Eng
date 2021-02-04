from settings import *

pygame.init()
font = pygame.font.Font(FONT, FONT_SIZE)


def display_text(text, surface, pos=(), color=BLACK, background=None):
    text_img = font.render(text, True, color, background)
    surface.blit(text_img, pos)


class LiteControlButton:
    """
    Есть проблема с перемещением объекта по оси У. проблема связана с выходом из цветового диапазона - нужно
    обратобать универсальность значения цвета с полажением ползунка.
    """

    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.R = 0
        self.G = 255
        self.B = 0
        self.button_y = 20
        self.x = x
        self.y = y
        self.color = DARK_GRAY
        self.active = False
        self.aria = pygame.Surface((w, h))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
                self.color = SKY_BLUE
                self.button_y = event.pos[-1] + (self.y - HEIGHT)
                self.R = self.button_y
                self.G = 225 - self.R
                print(self.button_y)  # tmp
                print(self.G, self.R)  # tmp
            else:
                self.active = False
                self.color = DARK_GRAY
                print('inactive')  # tmp

    def draw(self, screen):
        self.aria.fill((self.get_lite_value()))
        pygame.draw.rect(screen, self.color, self.rect, 5)
        pygame.draw.circle(self.aria, (self.R, self.G, self.B),
                           (self.rect.w // 2, self.button_y), (self.rect.w // 2), 20)
        screen.blit(self.aria, (self.x, self.y))

    def get_lite_value(self):
        return self.G, self.G, self.G


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = DARK_GRAY
        self.text = text
        self.txt_surface = font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = SKY_BLUE if self.active else DARK_GRAY
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:  # Вывод текст при нажатии Ентер.
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = font.render(self.text, True, self.color)

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.line(screen, self.color, (self.rect.x, self.rect.y + self.rect.h),
                         (self.rect.w, self.rect.y + self.rect.h), 2)


class TextDisplay:

    def __init__(self, text_file, surface, x, y):
        self.text_file = text_file
        self.surface = surface
        self.x = x
        self.y = y
        self.date = list()

    def displayed(self):
        pass

    def over_turned(self):
        pass

    def get_load_file(self):
        with open(self.text_file, 'r') as inf:
            date = inf.read().splitlines()
            self.date = date
