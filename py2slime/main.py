import pygame

from constants import *
import menu


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)

        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.display = pygame.Surface(tuple(map(lambda x: x * 15 // WINDOW_SCALE, WINDOW_SIZE)))
        self.clock = pygame.time.Clock()

        self.game_loop()

    def game_loop(self):
        menu.draw_start_screen(self.screen, self.display, self.clock)


if __name__ == "__main__":
    Game()
