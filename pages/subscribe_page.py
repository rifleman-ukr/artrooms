from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class SubscribePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self._subscribe_layout = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/subscribe_background_imageView")
        self._subscribe_title = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/subscribe_textView")
        self._back_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/back_from_subscribe_button")
        super().__init__(driver, self._subscribe_layout, self._back_button)

    def page_title(self):
        return self._get_element_text(self._subscribe_title)
