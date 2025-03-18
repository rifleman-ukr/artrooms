from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException


class BasePage:
    def __init__(self, driver, layout, back_button=None):
        self._driver = driver
        self._layout = layout
        self._back_button = back_button
        self._android_content_panel = (AppiumBy.ID, "android:id/contentPanel")

    def is_page_open(self):
        try:
            self._driver.find_element(*self._layout)
        except NoSuchElementException:
            return False
        else:
            return True

    def is_android_content_panel_displayed(self):
        try:
            self._driver.find_element(*self._android_content_panel)
        except NoSuchElementException:
            return False
        else:
            return True

    def system_back(self):
        self._driver.press_keycode(4)

    def go_back(self):
        if self._back_button:
            self._click_button(self._back_button)

    def _click_button(self, button):
        self._driver.find_element(*button).click()

    def _fill_text(self, text_field, text):
        self._driver.find_element(*text_field).send_keys(text)

    def _get_element_text(self, element):
        return self._driver.find_element(*element).text
