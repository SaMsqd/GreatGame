import pygame
import pygame_widgets
import controll


Run = True
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)


def Exit():
    pygame.quit()


def Return():
    global Run
    Run = False


def change_scene(number: int = 0):
    global Run
    controll.current_window_on_screen = number
    Run = False


def main_scene(screen, fps, widgets):
    controll.activate_widgets(widgets)
    while Run:
        events = pygame.event.get()
        screen.fill(WHITE)
        for event in events:
            if event.type == pygame.QUIT:
                break
        pygame_widgets.update(events)
        pygame.display.update()
        pygame.time.delay(fps)


def first_region(screen, fps, widgets):
    controll.activate_widgets(widgets)
    while Run:
        events = pygame.event.get()
        screen.fill(WHITE)
        pygame_widgets.update(events)
        pygame.display.update()
        pygame.time.delay(fps)


def second_region(screen, fps, widgets):
    controll.activate_widgets(widgets)
    while Run:
        events = pygame.event.get()
        screen.fill(WHITE)
        for event in events:
            if event.type == pygame.QUIT:
                change_scene(0)
        pygame_widgets.update(events)
        pygame.display.update()
        pygame.time.delay(fps)


def third_region(screen, fps, widgets):
    controll.activate_widgets(widgets)
    while Run:
        events = pygame.event.get()
        screen.fill(WHITE)
        for event in events:
            if event.type == pygame.QUIT:
                change_scene(0)
        pygame_widgets.update(events)
        pygame.display.update()
        pygame.time.delay(fps)


def fourth_region(screen, fps, widgets):
    controll.activate_widgets(widgets)
    while Run:
        events = pygame.event.get()
        screen.fill(WHITE)
        for event in events:
            if event.type == pygame.QUIT:
                change_scene(0)
        pygame_widgets.update(events)
        pygame.display.update()
        pygame.time.delay(fps)


scenes = {
    0: main_scene,
    1: first_region,
    2: second_region,
    3: third_region,
    4: fourth_region
}
