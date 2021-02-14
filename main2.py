# coding: utf-8
from settings import *
from objects import LiteControlButton, InputBox, TextDisplay, display_text


def main():
    sc = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Cyber_eng')
    pygame.display.set_icon(ICON)
    clock = pygame.time.Clock()
    done = False

    lite_control = LiteControlButton(10, 340)
    input_text = InputBox(10, 200, WIDTH - 10, 23)

    eng_text = TextDisplay(15, 250, WIDTH - 20, 3)
    eng_text.get_load_file(ENG_TEXT)

    while not done:
        for event in pygame.event.get():
            lite_control.handle_event(event)
            input_text.handle_event(event)
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:     #
                    eng_text.over_turned_up(True)    # временная штука проверяет работу перемотки
                if event.key == pygame.K_DOWN:   #
                    eng_text.over_turned_down()  #

        sc.fill((lite_control.get_lite_value()))
        lite_control.draw(sc)
        input_text.draw(sc)
        switch = input_text.check_text(eng_text.get_text())
        display_text('fps: ' + str(int(clock.get_fps())), sc, (WIDTH - 60, 10), TEXT_COLOR)
        eng_text.displayed(sc)
        eng_text.over_turned_up(switch)
        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
