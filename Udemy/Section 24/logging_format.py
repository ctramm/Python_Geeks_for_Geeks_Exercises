"""
Section 24: Lecture 143
Changing the format of logs

https://docs.python.org/3/library/logging.html#logrecord-attributes
https://docs.python.org/3/library/time.html#time.strftime
"""
import logging

logging.basicConfig(format='%(asctime)s :: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)
logging.warning("Warning Message")
logging.info("Info MSG")
logging.error("Error Message")
