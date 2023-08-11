from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait, Select


class DriverUtils:
    """
    Utility class to interact with the driver.
    """

    def __init__(self, driver: WebDriver, timeout: int) -> None:
        """
        Initialize the utility.
        :param driver: WebDriver object.
        :param timeout: default timeout for wait.
        """
        self.driver = driver
        self.timeout = timeout

    def __click_on_element(self, element: WebElement) -> None:
        self.driver.execute_script("arguments[0].click();", element)

    def __find_and_click(self, xpath: str) -> None:
        element = self.find_element_by_xpath(xpath)
        self.__click_on_element(element)

    def get_page(self, url: str) -> None:
        """
        Get a html page by URL.
        :param url: URL of the page to fetch.
        :return: None
        """
        self.driver.get(url)

    def find_element_by_xpath(self, xpath: str) -> WebElement:
        """
        Find an HTML element by XPATH.
        :param xpath: element's XPATH.
        :return: element.
        """
        return self.driver.find_element(By.XPATH, xpath)

    def wait_until_element_is_visible(self, xpath: str) -> None:
        """
        Wait until the element specified by xpath is visible.
        :param xpath:  element's XPATH.
        :return: None.
        """
        WebDriverWait(self.driver, self.timeout).until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath))
        )

    def wait_for_element_then_click(self, xpath) -> None:
        """
        Wait for element to be visible and then click on it.
        :param xpath: element's XPATH.
        :return: None.
        """
        self.wait_until_element_is_visible(xpath)
        self.__find_and_click(xpath)

    def wait_for_element_then_set_text_and_click_enter(
        self, xpath, text, is_in_iframe, i_frame_selector
    ) -> None:
        """
        Wait for the element to be visible, then enter text and press enter.
        :param xpath: element's xpath.
        :param text: text to enter.
        :param is_in_iframe: boolean flag indicating if the element is present inside an iFrame.
        :param i_frame_selector: if element is present inside an iFrame, this field is used to specify the iFrame's CSS selector.
        :return: None.
        """
        if is_in_iframe:
            self.driver.switch_to.frame(
                self.driver.find_element(By.CSS_SELECTOR, i_frame_selector)
            )
            self.wait_until_element_is_visible(xpath)
            element = self.find_element_by_xpath(xpath)
            element.send_keys(text)
            sleep(1)
            element.send_keys(Keys.ENTER)
            self.driver.switch_to.default_content()
        else:
            self.wait_until_element_is_visible(xpath)
            element = self.find_element_by_xpath(xpath)
            element.send_keys(text)
            sleep(1)
            element.send_keys(Keys.ENTER)

    def wait_for_element_then_select_value(self, xpath: str, value: str) -> None:
        """
        Wait for the element to be visible, then select one of the values.
        :param xpath: element's XPATH.
        :param value: value to select.
        :return: None.
        """
        self.wait_until_element_is_visible(xpath)
        select = Select(self.find_element_by_xpath(xpath))
        select.select_by_value(value)

    def save_screenshot(self, filename: str) -> None:
        """
        Take a screenshot of the current screen.
        :param filename: name of the file where the screenshot needs to be stored.
        :return: None.
        """
        self.driver.save_screenshot(filename)
