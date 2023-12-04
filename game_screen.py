import pygame
import pygame_gui
from pygame.locals import *

def draw_screen(screen, color):
    screen.fill(color)
    pygame.display.flip()

def switch_screen(current_screen):
    if current_screen == "screen1":
        return "screen2"
    elif current_screen == "screen2":
        return "screen1"

def main():
    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Game Example")

    manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

    button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                          text='Switch Screen',
                                          manager=manager)

    running = True
    current_screen = "screen1"

    clock = pygame.time.Clock()

    while running:
        time_delta = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    current_screen = switch_screen(current_screen)
            elif event.type == USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == button:
                        current_screen = switch_screen(current_screen)

            manager.process_events(event)

        manager.update(time_delta)

        draw_screen(screen, BLACK if current_screen == "screen1" else WHITE)

        manager.draw_ui(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
