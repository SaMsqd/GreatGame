import sys
import time
import pygame
import pygame_widgets

import colors
from pygame_widgets.button import Button, ButtonArray


def get_screen(data) -> pygame.display:  # Возвращает экран
    if data["window"] == "full":
        return pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
        scr_width = data["window"].split(",")[0]
        scr_height = data["window"].split(",")[1]
        return pygame.display.set_mode((scr_width, scr_height))


def get_data_from_cfg() -> dict:  # Читает файл cfg и возвращает словарь "параметр": "значение"
    data = dict()
    try:
        with open("cfg.txt", mode="r") as file:
            for line in file.readlines():
                setting_name = line.split("=")[0]
                setting_value = line.split("=")[1].replace("\n", "")
                data[setting_name] = setting_value
        return data
    except:
        time.sleep(5)
        print("Ошибка инициализации, пробую ещё раз")
        time.sleep(3)
        get_data_from_cfg()


def init():
    pygame.init()
    data = get_data_from_cfg()
    screen = get_screen(data)
    return screen


def main_loop(screen):
    while True:
        events = pygame.event.get()
        screen.fill(colors.WHITE)
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame_widgets.update(events)
        pygame.display.update()


def create_exit_button(screen):
    return Button(screen)
