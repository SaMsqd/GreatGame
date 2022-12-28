import pygame, pygame_widgets


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)


def main_scene(screen, fps):
    events = pygame.event.get()
    screen.fill(WHITE)
    for event in events:
        if event.type == pygame.QUIT:
            exit()
            return
    pygame_widgets.update(events)
    pygame.display.update()
    pygame.time.delay(fps)


def first_region():
    pass


def second_region():
    pass


def third_region():
    pass


def fourth_region():
    pass


scenes = {
    0: main_scene,
    1: first_region,
    2: second_region,
    3: third_region,
    4: fourth_region
}
