from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self._edit_menu_layout = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/edit_menu_layout")
        self._rotate_shadow_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/rotate_shadow_button")
        self._shadow_darkness_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/shadow_darkness_button")
        self._rotate_art_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/rotate_art_button")
        self._edit_done_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/edit_done_button")
        super().__init__(driver, self._edit_menu_layout)

    def rotate_shadow(self):
        self._click_button(self._rotate_shadow_button)

    def increase_shadow_darkness(self, amount):
        for _ in range(amount):
            self._click_button(self._shadow_darkness_button)

    def rotate_art(self):
        self._click_button(self._rotate_art_button)

    def finish_editing(self):
        self._click_button(self._edit_done_button)
