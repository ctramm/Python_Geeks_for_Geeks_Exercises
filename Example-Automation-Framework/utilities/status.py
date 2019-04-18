"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the result

Example:
    self.check_point.mark_final("Test Name", result, "Message")
"""
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class Status(SeleniumDriver):

    log = cl.custom_logger(logging.INFO)

    def __init__(self, driver):
        super(Status, self).__init__(driver)
        self.result_list = []

    def set_result(self, result, message):
        try:
            if result is not None:
                if result:
                    self.result_list.append("PASS")
                    self.log.info("### VERIFICATION PASSED :: + " + message)
                else:
                    self.result_list.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :: + " + message)
                    self.take_screenshot(message)
            else:
                self.result_list.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: + " + message)
                self.take_screenshot(message)
        except:
            self.result_list.append("FAIL")
            self.log.error("### EXCEPTION !!!")
            self.take_screenshot(message)

    def mark(self, result, message):
        """
        Mark the result of the verification point in a test case
        """
        self.set_result(result, message)

    def mark_final(self, test_name, result, message):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of test case
        """
        self.set_result(result, message)

        if "FAIL" in self.result_list:
            self.log.error(test_name + "### TEST FAILURE ### ")
            self.result_list.clear()
            assert False
        else:
            self.log.info(test_name + "### TEST PASSED")
            self.result_list.clear()
            assert True
