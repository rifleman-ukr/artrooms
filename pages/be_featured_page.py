from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class BeFeaturedPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self._be_featured_header_layout = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/be_featured_top_bar_imageView")
        self._be_featured_title = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/be_featured_title_textView")
        self._back_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/back_from_be_featured_button")
        self._submit_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/be_featured_button_done")
        self._text_field = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/be_featured_editText")
        super().__init__(driver, self._be_featured_header_layout, self._back_button)

    def page_title(self):
        return self._get_element_text(self._be_featured_title)

    def submit_form(self, text):
        self._fill_text(self._text_field, text)
        self._click_button(self._submit_button)
