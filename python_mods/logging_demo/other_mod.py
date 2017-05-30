import logging


def add(x, y):
    total = x + y
    logging.info('%s + %s = %s' % (x, y, total))
    return total
