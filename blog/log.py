import logging

def get_logger(name):
    return logging.getLogger(f'blog.{name}')