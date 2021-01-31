from settings import *
from objects import LiteControlButton, InputBox


def main():
    sc = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Cyber_eng')
    pygame.display.set_icon(ICON)
    font = pygame.font.Font(FONT, FONT_SIZE)
    clock = pygame.time.Clock()
    done = False

    lite_control = LiteControlButton(20, 300, 20, 225)
    input_text = InputBox(10, 200, WIDTH - 10, 23)

    while not done:
        for event in pygame.event.get():
            lite_control.handle_event(event)
            input_text.handle_event(event)
            if event.type == pygame.QUIT:
                done = True

        sc.fill((lite_control.get_lite_value()))
        lite_control.draw(sc)
        input_text.draw(sc)
        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
