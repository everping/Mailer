__author__ = 'Ping'

import logging

log_file = "log.txt"
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create file handler which logs even debug messages
fh = logging.FileHandler(log_file)
fh.setLevel(logging.INFO)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)
