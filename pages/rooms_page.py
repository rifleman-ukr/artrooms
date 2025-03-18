from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class RoomsPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self._rooms_layout = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/select_room_layout")
        self._back_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/back_from_room_button")
        self._filter_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/button_filter_room")
        self._import_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/button_import_room")
        self._all_rooms_parent = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/recyclerView_rooms")
        super().__init__(driver, self._rooms_layout, self._back_button)

    def open_filters(self):
        self._click_button(self._filter_button)

    def click_import(self):
        self._click_button(self._import_button)

    def get_filter_button_text(self):
        return self.driver.find_element(*self._filter_button).text

    def apply_filter(self, filter_name):
        self._click_button(self._filter_button)
        assert self.is_android_content_panel_displayed(), "Filter dialogue should be open"
        self.driver.find_element(AppiumBy.XPATH, f"//*[contains(@text, '{filter_name}')]").click()

    def choose_room(self, index=0):
        self._all_rooms()[index].click()

    def _all_rooms(self):
        rooms_parent = self.driver.find_element(*self._all_rooms_parent)
        return rooms_parent.find_elements(AppiumBy.CLASS_NAME, "android.view.ViewGroup")
