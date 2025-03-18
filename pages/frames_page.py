from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class FramesPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self._frames_header_layout = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/frame_top_bar_imageView")
        self._frames_title = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/frame_title_textView")
        self._back_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/back_from_frames_button")
        self._no_frame_button = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/button_no_frame")
        self._all_frames = (AppiumBy.ID, "com.artroomsapp.honuandroid:id/recyclerView_frames")
        super().__init__(driver, self._frames_header_layout, self._back_button)

    def page_title(self):
        return self._get_element_text(self._frames_title)

    def choose_no_frame(self):
        self._click_button(self._no_frame_button)

    def all_frames(self):
        frames_parent = self.driver.find_element(*self._all_frames)
        return frames_parent.find_elements((AppiumBy.CLASS_NAME, "android.view.ViewGroup"))
