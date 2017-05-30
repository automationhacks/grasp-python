import logging
import logging.config
import other_mod_2


def main():
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger('example')

    logger.info('program started')
    result = other_mod_2.add(8, 7)
    logger.info('done!')


if __name__ == '__main__':
    main()
