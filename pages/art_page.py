from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class ArtPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self._art_layout = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/select_art_layout")
        self._art_title = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/title_textView")
        self._back_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/back_from_art_button")
        self._import_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/button_import_art")
        self._all_arts_view = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/recyclerView_arts")
        super().__init__(driver, self._art_layout, self._back_button)

    def page_title(self):
        return self._get_element_text(self._art_title)

    def click_import(self):
        self._click_button(self._import_button)

    def are_units_metric(self):
        if "cm" in self._all_arts()[0].find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")[1].text:
            return True

    def return_to_main_page(self):
        self.go_back()

    def _all_arts(self):
        arts_parent = self.driver.find_element(*self._all_arts_view)
        return arts_parent.find_elements(AppiumBy.CLASS_NAME, "android.view.ViewGroup")
