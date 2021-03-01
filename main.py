from DMXHunterThread import DMXHunterThread


def main():
    hunter = DMXHunterThread()
    hunter.start()
    hunter.join()


if __name__ == '__main__':
    main()
