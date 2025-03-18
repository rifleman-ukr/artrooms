from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage
from pages.menu_page import MenuPage


class SettingsPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self._settings_layout = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/orange_imageView_settings")
        self._back_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/back_from_settings_button")
        self._current_units_label = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/measure_textview")
        self._change_units_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/change_measure_button")
        self._manage_subscriptions_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/managesubscription_button")
        self._policy_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/policy_button")
        self._invite_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/menu_invite_button")
        super().__init__(driver, self._settings_layout, self._back_button)

    def are_units_metric(self):
        if "metric" in self._get_element_text(self._current_units_label):
            return True

    def change_units(self):
        self._click_button(self._change_units_button)

    def click_manage_subscriptions(self):
        self._click_button(self._manage_subscriptions_button)

    def open_privacy_policy(self):
        self._click_button(self._policy_button)

    def click_share(self):
        self._click_button(self._invite_button)

    def return_to_main_page(self):
        self.go_back()
        MenuPage(self.driver).go_back()
