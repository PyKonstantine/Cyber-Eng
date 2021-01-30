# -*- coding: utf-8 -*-
from settings import *
from googletrans import Translator

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))  # создает окно по габаритам
clock = pygame.time.Clock()  # экцемплятор объекта - установка колличества кадров в секунду
pygame.display.set_caption('Cyber_eng')  # название окна
pygame.display.set_icon(ICON)  # иконка окна
font = pygame.font.Font(FONT, FONT_SIZE)  # создает объект текста(шрифт, размер)


def display_text(text, pos=(), surface=sc, color=BLACK, background=None):
    """
    Отображает полученный текст на указанном поверхности

    :return смещение по оси Х в пикселях
    """
    text_img = font.render(text, True, color, background)
    surface.blit(text_img, pos)
    return text_img.get_rect().right


def interface():
    pygame.draw.line(sc, SKY_BLUE, (10, 230), (WIDTH - 10, 230), 1)
    fps = int(clock.get_fps())
    display_text('fps: ' + str(fps), (WIDTH - 60, 10), sc, SKY_BLUE)
    display_text('счетчик: ' + str(count), (20, 20), sc, SKY_BLUE)


def text_writer(text):
    """
    Принимает текст и отображает его в поле ввода.

    сравнивает вводимый текст с исходным окрашивает в красный, если не равны.
    очищает вводимую строку и вынимает из хаба строку, если текст дописан доконца и соответствует исходному
    """
    process_point = len(text)
    pos = (15, 206)
    bg = None
    global input_text
    if text != eng_text_hab[0][:process_point]:
        bg = RED
    rect = display_text(text, pos, sc, SKY_BLUE, bg)
    if rect > rect_equal and text == eng_text_hab[0] + ' ':
        eng_text_hab.pop(0)
        input_text = ''


def get_text(doc, mode='r'):
    with open(doc, mode) as inf:
        date = inf.read().splitlines()
        return date


def display_eng_text(hab):
    """
    Отображает 3 строки текста
    """
    global rect_equal, count
    while len(hab) < 3:
        hab.append(eng_text[count].strip())
        count += 1
    text_aria = pygame.Surface((WIDTH - 20, 80))
    text_aria.fill(BACKGROUND)
    rect_equal = display_text(hab[0], (0, 0), text_aria, SKY_BLUE)
    display_text(hab[1], (0, 20), text_aria, SKY_BLUE)
    display_text(hab[2], (0, 40), text_aria, SKY_BLUE)
    sc.blit(text_aria, (15, 250))


def trans_text_writer():
    counter = len(input_text.split())  # счетчик генерируется каждым пробелом в стороке. Надо пофиксить - артикли.
    b = trans_text[count - 3]
    c = str(b).split()
    text = ' '.join(c[:counter - 1])
    rect = display_text(text, (15, 160), sc, SKY_BLUE)
    if rect > rect_equal:
        text = text[1:]


def translation_text():
    if trans_text == list():
        translator = Translator()
        with open('text.txt', 'r') as inf:
            contents = inf.read()
            result = translator.translate(contents, src='en', dest='ru')
            result_text = result.text

        with open('translation text.txt', 'w') as f:
            f.write(result_text)


input_text = str()  # хранит вводимый текст в одну строку.
trans_text = get_text(TRANS_TEXT)
eng_text = get_text(ENG_TEXT)
translation_text()  # если док с переводом пуст - считывает, переводит и записывает текст.
eng_text_hab = []  # хранит три строки ин.текста в структуре очереди.
rect_equal = 0  # хранит значение длинны вводимой строки для сравнения с ин.строкой. Нуждна для очищения если =
count = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            input_text += event.unicode
            if event.key == pygame.K_UP:  # временная процедура!!!
                input_text = ''
                eng_text_hab.pop(0)

    sc.fill(BACKGROUND)
    display_eng_text(eng_text_hab)
    text_writer(input_text)
    trans_text_writer()
    interface()
    pygame.display.update()
    clock.tick(FPS)
