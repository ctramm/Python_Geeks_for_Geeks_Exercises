"""
Section 24: Intro to Logging

Logging Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
"""
import logging

# logging.warning("Warning Message")
# logging.info("Information Message")
#
# # Default Threshold set to Warning, which includes Warning, Error, Critical.
#
# logging.error("Error Message")

logging.basicConfig(filename="test.log", level=logging.DEBUG)

logging.warning("Warning Message")
logging.info("Information Message")
logging.error("Error Message")

