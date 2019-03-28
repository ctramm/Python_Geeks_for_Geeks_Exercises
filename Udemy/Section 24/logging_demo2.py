"""
Section 24: Lecture 146 - How to write a generic custom logger utility
"""
import logging
import Udemy.Utils.custom_logger as cl


class LoggingDemo2:

    log = cl.custom_logger(logging.DEBUG)

    def method1(self):
        self.log.debug('debug message')
        self.log.info('info message')
        self.log.warning('warning message')
        self.log.error('error message')
        self.log.critical('critical message')

    def method2(self):
        m2Log = cl.custom_logger(logging.CRITICAL)
        m2Log.debug('debug message')
        m2Log.info('info message')
        m2Log.warning('warning message')
        m2Log.error('error message')
        m2Log.critical('critical message')

    def method3(self):
        m3Log = cl.custom_logger(logging.INFO)
        m3Log.debug('debug message')
        m3Log.info('info message')
        m3Log.warning('warning message')
        m3Log.error('error message')
        m3Log.critical('critical message')


demo = LoggingDemo2()
demo.method1()
demo.method2()
demo.method3()
