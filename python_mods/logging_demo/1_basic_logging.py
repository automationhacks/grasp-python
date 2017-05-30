import logging
# logging.getLogger(__name__).addHandler(logging.NullHandler())

# Logging levels DEBUG > INFO > WARNING > ERROR > CRITICAL

logging.basicConfig(filename='sample.log', level=logging.INFO)
logging.debug('debug message')  # This will not get logged
logging.info('info message')
logging.error('error message')
