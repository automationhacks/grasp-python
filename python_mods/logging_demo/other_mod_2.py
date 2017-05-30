import logging

module_logger = logging.getLogger('example.other_mod_2')


def add(x, y):
    logger = logging.getLogger('example.other_mod_2.add')
    total = x + y
    logger.info('added %s and %s to get %s' % (x, y, total))
    return total
