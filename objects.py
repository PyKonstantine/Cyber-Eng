from settings import *

pygame.init()
font = pygame.font.Font(FONT, FONT_SIZE)


def display_text(text, surface, pos, color=BLACK, background=None):
    text_img = font.render(text, True, color, background)
    surface.blit(text_img, pos)


class LiteControlButton:
    """
    Есть проблема с перемещением объекта по оси У. проблема связана с выходом из цветового диапазона - нужно
    обратобать универсальность значения цвета с полажением ползунка.
    """

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

    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = DARK_GRAY
        self.text = ''
        self.txt_surface = font.render(self.text, True, self.color)
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
        self.txt_surface = font.render(self.text, True, self.color, self.bg)
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
    """
    Объект отображает текст на на заданной поверхности

    процесс:
    - нужен метод для сравнения равенства отображаемой строки с вводимым текстом в объекте InputBox
    """

    def __init__(self, x, y, width, str_num=1):
        self.rect = pygame.Rect(x, y, width, str_num * FONT_SIZE)  # колличество строк ?
        self.str_num = str_num
        self.date = list()
        self.text_counter = 0

    def get_load_file(self, text_file):
        with open(text_file, 'r') as inf:
            date = inf.read().splitlines()
            self.date = date

    def displayed(self, surface, color=TEXT_COLOR, background=None):
        for i in range(self.str_num):
            text_img = font.render(self.date[self.text_counter + i], True, color, background)
            surface.blit(text_img, (self.rect.x, self.rect.y + (FONT_SIZE - 6) * i))

    def get_text(self):
        return self.date[self.text_counter]

    def over_turned_up(self, switch):
        if switch:
            self.text_counter += 1

    def over_turned_down(self):
        self.text_counter -= 1

