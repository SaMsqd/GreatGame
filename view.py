import controll

def main():
    screen = controll.init()
    controll.main_loop(screen)
    controll.create_exit_button(screen)


if __name__ == "__main__":
    main()
