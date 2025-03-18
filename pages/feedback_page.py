from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class FeedbackPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self._feedback_header_layout = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/feedback_top_bar_imageView")
        self._feedback_title = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/feedback_title_textView")
        self._back_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/back_from_feedback_button")
        self._send_feedback_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/feedback_button_done")
        self._name_field = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/feedback_name_editText")
        self._feedback_text_field = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/feedback_editText")
        super().__init__(driver, self._feedback_header_layout, self._back_button)

    def page_title(self):
        return self._get_element_text(self._feedback_title)

    def send_feedback(self, name, text):
        self._fill_text(self._name_field, name)
        self._fill_text(self._feedback_text_field, text)
        self._click_button(self._send_feedback_button)
