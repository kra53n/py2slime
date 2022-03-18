import pygame

WINDOW_SCALE = 120
WINDOW_SIZE = (16 * WINDOW_SCALE, 9 * WINDOW_SCALE)
WINDOW_TITLE = "py2slime"

IMAGES_PATH = "assets/images/"
TITLE_IMAGE = pygame.image.load(IMAGES_PATH + "title_image.png")
BUTTONS = {
    "non_active": pygame.image.load(IMAGES_PATH + "non_active_button.png")
}