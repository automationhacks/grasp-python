import logging
import other_mod


def main():
    logging.basicConfig(filename='my_snake.log', level=logging.INFO)
    logging.info('program started')
    result = other_mod.add(7, 8)
    logging.info('done!')


if __name__ == '__main__':
    main()
