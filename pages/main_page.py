from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self._main_activity_layout = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/main_activity_layout")
        self._menu_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/menu_button")
        self._rooms_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/rooms_button")
        self._art_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/art_button")
        self._frames_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/frames_button")
        self._export_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/export_button")
        self._edit_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/edit_button")
        super().__init__(driver, self._main_activity_layout)

    def open_menu(self):
        self._click_button(self._menu_button)

    def open_rooms(self):
        self._click_button(self._rooms_button)

    def open_art(self):
        self._click_button(self._art_button)

    def open_frames(self):
        self._click_button(self._frames_button)

    def open_export(self):
        self._click_button(self._export_button)

    def open_edit(self):
        self._click_button(self._edit_button)
