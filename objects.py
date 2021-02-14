from settings import *
from fonts import fonts

pygame.init()


class FontControlButton:
    Fonts = fonts

    def __init__(self, x, y):
        self.width = 32
        self.height = 40
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.active = False
        self.font_counter = 3
        self.font = FontControlButton.Fonts[self.font_counter]
        self.size_font = 18
        self.color = DARK_GRAY
        self.font_collection = len(FontControlButton.Fonts)
        self.FONT = pygame.font.SysFont(self.font, self.size_font, True)
        self.load = pygame.image.load('img/2.png')
        self.icon = pygame.transform.scale(self.load, (100, 100))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
                self.color = TEXT_COLOR
            else:
                self.active = False
                self.color = DARK_GRAY
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_UP:
                    self.size_font += 1
                    self.FONT = pygame.font.SysFont(self.font, self.size_font, True)
                if event.key == pygame.K_DOWN:
                    self.size_font -= 1
                    self.FONT = pygame.font.SysFont(self.font, self.size_font, True)
                if event.key == pygame.K_LEFT:
                    self.font_counter -= 1
                    self.font = FontControlButton.Fonts[self.font_counter]
                    self.FONT = pygame.font.SysFont(self.font, self.size_font, True)
                if event.key == pygame.K_RIGHT:
                    if self.font_counter < self.font_collection:
                        self.font_counter += 1
                        self.font = FontControlButton.Fonts[self.font_counter]
                        self.FONT = pygame.font.SysFont(self.font, self.size_font, True)

    def draw(self, surface):
        surface.blit(self.icon, (self.rect.x - 34, self.rect.y - 34))
        pygame.draw.rect(surface, self.color, self.rect, 5)

    def get_font(self):
        return self.FONT


font_control = FontControlButton(50, 50)


def display_text(text, surface, pos, color=BLACK, background=None):
    text_img = font_control.get_font().render(text, True, color, background)
    surface.blit(text_img, pos)


class LiteControlButton:

    def __init__(self, x, y, w=20, h=255):
        self.rect = pygame.Rect(x, y, w, h)
        self.R = 0
        self.G = 255
        self.B = 0
        self.button_y = 0
        self.x = x
        self.y = y
        self.color = DARK_GRAY
        self.active = False
        self.aria = pygame.Surface((w, h))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
                self.color = TEXT_COLOR
                self.button_y = event.pos[-1] - self.y
                self.R = self.button_y
                self.G = 255 - self.R
                print(f'значение button_y: {self.button_y}')  # tmp
                print(f'значение G:{self.G}\nзначение R:{self.R}')  # tmp
            else:
                self.active = False
                self.color = DARK_GRAY

    def draw(self, screen):
        self.aria.fill((self.get_lite_value()))
        pygame.draw.rect(screen, self.color, self.rect, 5)
        pygame.draw.circle(self.aria, (self.R, self.G, self.B),
                           (self.rect.w // 2, self.button_y), (self.rect.w // 2), 10)
        screen.blit(self.aria, (self.x, self.y))

    def get_lite_value(self):
        return self.G, self.G, self.G


class InputBox:

    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = DARK_GRAY
        self.text = ''
        self.txt_surface = font_control.get_font().render(self.text, True, self.color)
        self.active = False
        self.bg = None

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = TEXT_COLOR if self.active else DARK_GRAY
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:  # Вывод текст при нажатии Ентер.
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self, screen):
        self.txt_surface = font_control.get_font().render(self.text, True, self.color, self.bg)
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.line(screen, self.color, (self.rect.x, self.rect.y + self.rect.h),
                         (self.rect.w, self.rect.y + self.rect.h), 2)

    def check_text(self, check_string):
        processing = len(self.text)
        if check_string + ' ' == self.text:
            self.text = ''
            return True
        elif self.text != check_string[:processing]:
            self.bg = RED
        else:
            self.bg = None
            return False


class TextDisplay:

    def __init__(self, x, y, width, str_num=1):
        self.rect = pygame.Rect(x, y, width, str_num * FONT_SIZE)  # колличество строк ?
        self.str_num = str_num
        self.date = list()
        self.text_counter = 0
        self.active = False

    def get_load_file(self, text_file):
        with open(text_file, 'r') as inf:
            date = inf.read().splitlines()
            self.date = date

    def displayed(self, surface, color=TEXT_COLOR, background=None):
        for i in range(self.str_num):
            text_img = font_control.get_font().render(self.date[self.text_counter + i], True, color, background)
            surface.blit(text_img, (self.rect.x, self.rect.y + (FONT_SIZE - 6) * i))
        if self.active:
            pygame.draw.rect(surface, color, self.rect, 3)

    def get_text(self):
        return self.date[self.text_counter]

    def over_turned_up(self, switch):
        if switch:
            self.text_counter += 1

    def over_turned_down(self):
        self.text_counter -= 1

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_UP:
                    self.text_counter += 1
                if event.key == pygame.K_DOWN:
                    self.text_counter -= 1
