from settings import *
from objects import *


lite_control = LiteControlButton(20, 300, 20, 225)


def main():
    sc = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Cyber_eng')
    pygame.display.set_icon(ICON)
    font = pygame.font.Font(FONT, FONT_SIZE)
    clock = pygame.time.Clock()
    done = False

    while not done:
        for event in pygame.event.get():
            lite_control.handle_event(event)
            if event.type == pygame.QUIT:
                done = True

        sc.fill((lite_control.get_lite_value()))
        lite_control.draw(sc)
        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
