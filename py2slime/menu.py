import sys
import pygame

from constants import (
    WINDOW_SIZE,
    TITLE_IMAGE,
    BUTTONS,
)


def draw_title_image(display):
    display.blit(
        TITLE_IMAGE,
        (
            (display.get_width() - TITLE_IMAGE.get_width()) // 2,
            (display.get_height() - TITLE_IMAGE.get_height()) // 2 - 10,
        )
    )


def draw_button(display, action):
    display.blit(
        BUTTONS[action],
        (
            (display.get_width() - BUTTONS["non_active"].get_width()) // 2,
            display.get_height() // 2 + 10,
        )
    )


def draw_start_screen(screen, display, clock):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        display.fill((55, 33, 52))

        draw_title_image(display)
        draw_button(display, "non_active")

        screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))
        pygame.display.update()
        clock.tick(60)
