"""
Section 24: Lecture 145 - Configuration File Example
"""

import logging
import logging.config


class LoggerConsoleConf:

    def log_test(self):
        # Create Logger
        logging.config.fileConfig('logging.conf')
        logger = logging.getLogger(LoggerConsoleConf.__name__)

        # Logging Messages
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')


demo = LoggerConsoleConf()
demo.log_test()
