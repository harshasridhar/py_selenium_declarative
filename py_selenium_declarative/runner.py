import logging
from re import match
from time import sleep, time

from selenium.webdriver.chrome.webdriver import WebDriver

from py_selenium_declarative.constants import Constants
from py_selenium_declarative.driver_utils import DriverUtils
from py_selenium_declarative.model.operation import Operation
from py_selenium_declarative.model.suite import Suite


class Runner:
    driver_utils: DriverUtils = None
    logger = None

    def __init__(self, driver: WebDriver, timeout: int) -> None:
        self.driver_utils = DriverUtils(driver, timeout)
        self.logger = logging.getLogger(__name__)

    def run(self, suite: Suite) -> None:
        """
        Runs the provided test suite.
        :param suite: Test suite to run.
        :return: None
        """
        for operation in suite.operations:
            try:
                self.__run_operation__(operation)
                self.logger.info("Operation done %s", operation)
            except Exception as ex:
                self.logger.error("Operation failed %s", operation)
                self.driver_utils.save_screenshot(f"failure_{operation.name}.png")
                raise ex

    def __run_operation__(self, operation: Operation) -> None:
        if operation.action == Constants.ACTION_TYPE_GET:
            self.driver_utils.get_page(operation.value)
        if operation.action == Constants.ACTION_TYPE_CLICK:
            self.driver_utils.wait_for_element_then_click(operation.xpath)
        elif operation.action == Constants.ACTION_TYPE_TEXT:
            if operation.verify:
                self.driver_utils.wait_until_element_is_visible(operation.xpath)
                element = self.driver_utils.find_element_by_xpath(operation.xpath)
                matches = (
                    bool(match(operation.value, element.text))
                    if "*" in operation.value
                    else operation.value == element.text
                )
                if not matches:
                    raise Exception(
                        "Expected: [{}] Found [{}] ".format(
                            operation.value, element.text
                        )
                    )
            else:
                self.driver_utils.wait_for_element_then_set_text_and_click_enter(
                    operation.xpath,
                    operation.value,
                    operation.isInIFrame,
                    operation.iFrameSelector,
                )
        elif operation.action == Constants.ACTION_TYPE_SELECT:
            self.driver_utils.wait_for_element_then_select_value(
                operation.xpath, operation.value
            )
        elif operation.action == Constants.ACTION_TYPE_SLEEP:
            self.logger.info("Sleep started at %s", time())
            sleep(int(operation.value))
            self.logger.info("Sleep ended at %s", time())
        elif operation.action == Constants.ACTION_TYPE_SCREENSHOT:
            filename = f'screenshot_{operation.name if operation.name != "" else int(time())}.png'
            self.driver_utils.save_screenshot(filename)
