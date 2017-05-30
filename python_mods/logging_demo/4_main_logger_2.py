import logging
import other_mod_2


def main():
    logger = logging.getLogger('example')
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler('my_snake_2.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    logger.info('program started')
    result = other_mod_2.add(7, 8)
    logger.info('Done!')


if __name__ == '__main__':
    main()
