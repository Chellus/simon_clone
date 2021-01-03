import pygame
import random

pygame.init()

# window constants
WINDOW_W = 600
WINDOW_H = 600

# window and clock
window = pygame.display.set_mode((WINDOW_W, WINDOW_H))
clock = pygame.time.Clock()

# colors
BLACK = (0, 0, 0)
RED = (175, 0, 0)
GREEN = (0, 175, 0)
BLUE = (0, 0, 175)
YELLOW = (175, 175, 0)
BRIGHT_RED = (255, 0, 0)
BRIGHT_GREEN = (0, 255, 0)
BRIGHT_BLUE = (0, 0, 255)
BRIGHT_YELLOW = (255, 255, 0)

# game loop function
def game_loop():
    running = True
    buttons_order = [] # in this list we store the order in which you need to touch the buttons

    yellow_rect = pygame.Rect(100, 100, 195, 195)
    blue_rect = pygame.Rect(305, 100, 195, 195)
    red_rect = pygame.Rect(100, 305, 195, 195)
    green_rect = pygame.Rect(305, 305, 195, 195)

    window.fill(BLACK)

    while running:
        # for every event
        for event in pygame.event.get():
            # if the event is a quit event, quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                running = False

        pygame.draw.rect(window, YELLOW, yellow_rect)
        pygame.draw.rect(window, BLUE, blue_rect)
        pygame.draw.rect(window, GREEN, green_rect)
        pygame.draw.rect(window, RED, red_rect)

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    game_loop()
