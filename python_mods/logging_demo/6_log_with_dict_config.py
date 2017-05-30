import logging
import logging.config
import other_mod_2


def main():
    log_config_dict = {
        'version': 1,
        'handlers': {
            'fileHandler': {
                'class': 'logging.FileHandler',
                'formatter': 'myFormatter',
                'filename': 'config2.log'
            }

        },
        'loggers': {
            'example': {
                'handlers': ['fileHandler'],
                'level': 'INFO'
            }
        },
        'formatters': {
            'myFormatter': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            }
        }
    }

    logging.config.dictConfig(log_config_dict)
    logger = logging.getLogger('example')
    logger.info('program started')
    result = other_mod_2.add(10 , 20)
    logger.info('done!')

if __name__ == '__main__':
    main()

