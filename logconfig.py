
import logging
import logging.config

logging.config.fileConfig('./instance/logging.conf')

# create logger
logger = logging.getLogger('Cognitive-API')

# 'application' code
'''
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
'''