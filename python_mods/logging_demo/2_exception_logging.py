"""
Logging exceptions
"""
import logging

logging.basicConfig(filename='sample.log', level=logging.INFO)
log = logging.getLogger('ex')

try:
    raise RuntimeError
except Exception as e:
    log.exception('Error!!!')

