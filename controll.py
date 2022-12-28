import time
import pygame
import pygame_widgets
import colors_and_scenes
from pygame_widgets.button import Button, ButtonArray

secondary_thread_alive = True

current_windown_on_screen = 0


def exit():
    pygame.quit()


def get_screen(data) -> pygame.Surface:  # Возвращает экран
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


def init() -> pygame.Surface:
    pygame.init()
    data = get_data_from_cfg()
    screen = get_screen(data)
    return screen


def main_loop(screen, *args) -> None:
    fps = int(get_data_from_cfg()["delay"])
    try:
        while True:
            colors_and_scenes.scenes[current_windown_on_screen](screen, fps)
    except: return


def create_exit_button(screen):
    width = 60
    height = 50
    x = pygame.display.get_window_size()[0] - width
    y = pygame.display.get_window_size()[1] - height
    return Button(screen, x, y, width, height, text="quit", onClick=exit)


def default_click_func(number: int) -> None:
    print(f"Кнопка была нажата {number}")


def create_regions(screen: pygame.Surface, count: int = 4, text: str = list(), on_click_funcs: list = list(),
                   on_click_params: list = list()) -> pygame_widgets.button.ButtonArray:
    if len(text) != count:
        for i in range(count+1):
            text.append(f"{i} region")
    if len(on_click_funcs) != count:
        for i in range(count+1):
            on_click_funcs.append(default_click_func)
    if len(on_click_params) != count:
        on_click_params = [[i] for i in range(0, count+1)]
    return ButtonArray(
        screen,
        0, 0,
        screen.get_size()[0] // 2, screen.get_size()[1] // 2,
        (2, count//2),
        font=pygame.font.SysFont("arial", 30),
        border=1,
        texts=text,
        onClicks=on_click_funcs,
        onClickParams=on_click_params,
    )


def secondary_thread():
    while secondary_thread_alive:
        print("Второй поток")
        time.sleep(1)
    print("Второй поток кончился")
