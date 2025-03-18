from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class MenuPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self._menu_layout = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/orange_imageView")
        self._back_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/back_from_menu_button")
        self._settings_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/settings_button")
        self._subscribe_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/menu_subscribe_button")
        self._feedback_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/menu_feedback_button")
        self._be_featured_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/menu_be_featured_button")
        self._invite_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/menu_invite_button")
        super().__init__(driver, self._menu_layout, self._back_button)

    def open_settings(self):
        self._click_button(self._settings_button)

    def open_subscribe_page(self):
        self._click_button(self._subscribe_button)

    def open_feedback_form(self):
        self._click_button(self._feedback_button)

    def open_be_featured_form(self):
        self._click_button(self._be_featured_button)

    def open_invite_page(self):
        self._click_button(self._invite_button)
