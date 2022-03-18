import pygame

from constants import *
import menu


def init():
    pygame.init()
    pygame.display.set_caption(WINDOW_TITLE)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    display = pygame.Surface(tuple(map(lambda x: x * 15 // WINDOW_SCALE, WINDOW_SIZE)))
    clock = pygame.time.Clock()
    return screen, display, clock


def game_loop():
    screen, display, clock = init()
    menu.draw_start_screen(screen, display, clock)


if __name__ == "__main__":
    game_loop()
