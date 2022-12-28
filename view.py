import controll
import threading


def main():
    screen = controll.init()
    secondary_thread = threading.Thread(target=controll.secondary_thread)
    # secondary_thread.start()
    controll.main_loop(screen)
    print("mainloop кончился")
    controll.secondary_thread_alive = False


if __name__ == "__main__":
    main()
