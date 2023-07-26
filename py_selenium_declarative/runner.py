import logging
from time import sleep, time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait, Select

from py_selenium_declarative.model.operation import Operation
from py_selenium_declarative.model.suite import Suite


class Runner:
    driver: WebDriver = None
    logger = None

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def run(self, suite: Suite):
        for operation in suite.operations:
            try:
                self.__run_operation__(operation)
                self.logger.info("Operation done %s", operation)
            except Exception as ex:
                self.logger.error("Operation failed %s", operation)
                self.driver.save_screenshot(f'failure_{operation.name}.png')
                raise ex

    def __run_operation__(self, operation: Operation) -> None:
        if operation.action == 'get':
            self.driver.get(operation.value)
        if operation.action == 'click':
            self.__wait_for_element_then_click__(operation.xpath)
        elif operation.action == 'text':
            self.__wait_for_element_then_set_text_and_click_enter__(operation.xpath, operation.value,
                                                                    operation.isInIFrame, operation.iFrameSelector)
        elif operation.action == 'select':
            self.__wait_for_element_then_select_value(operation.xpath, operation.value)
        elif operation.action == "sleep":
            self.logger.info("Started at %s", time())
            sleep(int(operation.value))
            self.logger.info("Ended at %s", time())
        elif operation.action == 'screenshot':
            filename = f'screenshot_{operation.name if operation.name != "" else int(time())}.png'
            self.driver.save_screenshot(filename)

    def __wait_until_element_is_visible__(self, xpath):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located((By.XPATH, xpath)))

    def __find_and_click__(self, xpath):
        element = self.driver.find_element(By.XPATH, xpath)
        self.driver.execute_script("arguments[0].click();", element)

    def __wait_for_element_then_click__(self, xpath):
        self.__wait_until_element_is_visible__(xpath)
        self.__find_and_click__(xpath)

    def __wait_for_element_then_set_text_and_click_enter__(self, xpath, text, is_in_iframe, i_frame_selector):
        if is_in_iframe:
            self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, i_frame_selector))
            self.__wait_until_element_is_visible__(xpath)
            element = self.driver.find_element(By.XPATH, xpath)
            element.send_keys(text)
            sleep(1)
            element.send_keys(Keys.ENTER)
            self.driver.switch_to.default_content()
        else:
            self.__wait_until_element_is_visible__(xpath)
            element = self.driver.find_element(By.XPATH, xpath)
            element.send_keys(text)
            sleep(1)
            element.send_keys(Keys.ENTER)

    def __wait_for_element_then_select_value(self, xpath, value):
        self.__wait_until_element_is_visible__(xpath)
        select = Select(self.driver.find_element(By.XPATH, xpath))
        select.select_by_value(value)
