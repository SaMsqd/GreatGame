import controll
import threading


def main():
    screen = controll.init()
    secondary_thread = threading.Thread(target=controll.secondary_thread)
    controll.create_exit_button(screen)
    secondary_thread.start()
    controll.main_loop(screen)
    print("mainloop кончился")
    controll.secondary_thread_alive = False


if __name__ == "__main__":
    main()
