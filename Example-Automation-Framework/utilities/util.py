"""
@package utilities

Util class Implementation
All most commonly used utilities should be implemented in this class

Example:
    name = self.util.get_unique_name()
"""
import logging
import random
import string
import time
import utilities.custom_logger as cl


# noinspection PyMethodMayBeStatic
class Util(object):

    log = cl.custom_logger(logging.INFO)

    def sleep(self, sec, info=""):
        """
        Put the program to wait for the specified amount of time
        """
        if info is not None:
            self.log.info("Wait :: '" + str(sec) + "' seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError as e:
            self.log.error(e)

    def get_alpha_numeric(self, length, type='letters'):
        """
        Get random string of characters
        """
        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def get_unique_name(self, char_count=10):
        """
        Get a unique name
        """
        return self.get_alpha_numeric(char_count, 'lower')

    def get_unique_name_list(self, list_size=5, item_length=None):
        """
        Get a list of valid email ids
        :param list_size: Number of names. Default is 5 names in a list
        :param item_length: It should be a list containing number of items equal to the list size
            This determines the length of each item in the list -> [1, 2, 3, 4, 5]
        :return:
        """
        name_list = []
        for i in range(0, list_size):
            name_list.append(self.get_unique_name(item_length[i]))
        return name_list

    def verify_text_contains(self, actual_text, expected_text):
        """
        Verify actual text contains expected text string
        :param actual_text:
        :param expected_text:
        :return:
        """
        self.log.info("Actual text from application web ui --> :: " + actual_text)
        self.log.info("Expected text from application web ui --> :: " + expected_text)
        if expected_text.lower() in actual_text.lower():
            self.log.info("### VERIFICATION TEXT CONTAINS !!!")
            return True
        else:
            self.log.info("### VERIFICATION TEXT DOES NOT CONTAIN !!!")
            return False

    def verify_text_match(self, actual_text, expected_text):
        """
        Verify text match
        :param actual_text:
        :param expected_text:
        :return:
        """
        self.log.info("Actual text from application web ui --> :: " + actual_text)
        self.log.info("Expected text from application web ui --> :: " + expected_text)
        if actual_text.lower() == expected_text.lower():
            self.log.info("### VERIFICATION TEXT MATCH !!!")
            return True
        else:
            self.log.info("### VERIFICATION TEXT DOES NOT MATCH !!!")
            return False

    def verify_list_match(self, expected_list, actual_list):
        """
        Verify two lists match
        :param expected_list:
        :param actual_list:
        :return:
        """
        return set(expected_list) == set(actual_list)

    def verify_list_contains(self, expected_list, actual_list):
        """
        Verify actual list contains elements of expected list
        :param expected_list:
        :param actual_list:
        :return:
        """
        length = len(expected_list)
        for i in range(0, length):
            if expected_list[i] not in actual_list:
                return False
        else:
            return True
