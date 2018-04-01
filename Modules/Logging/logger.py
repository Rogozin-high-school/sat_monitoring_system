# This serves as a static log object
# you can use this methods to write to log from module

from . import log
from . import config

logger = log.log(config.LOG_FILE_NAME)

def write(text):
    """ Writes to the default log file """
    log_object.write_to_log(text)

def read():
    """ Reads the default log file """
    return log_object.read_from_log()

def get_logger():
    """ Returns an object representing the default log file """
    return logger
