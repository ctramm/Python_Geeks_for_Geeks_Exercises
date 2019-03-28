"""
Section 24: Lecture 144 - Logger Console Example
"""
import logging


class LoggerConsole:

    def log_test(self):
        # Create Logger
        logger = logging.getLogger(LoggerConsole.__name__)
        logger.setLevel(logging.INFO)

        # Create Console Handler and set level to info
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Create Formatter
        formatter = logging.Formatter('%(asctime)s :: %(name)s :: %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        # Add formatter to console handler -> ch
        console_handler.setFormatter(formatter)

        # Add console handler to logger
        logger.addHandler(console_handler)

        # Logging Messages
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')


demo = LoggerConsole()
demo.log_test()
