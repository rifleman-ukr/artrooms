import os

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from utilities.config import config


@pytest.fixture(scope="session", autouse=True)
def driver():
    desired_capabilities = {
        "platformName": config.get("ANDROID", "PLATFORM"),
        "deviceName": config.get("ANDROID", "DEVICE"),
        "automationName": config.get("ANDROID", "AUTOMATION"),
        "app": os.path.join(os.getcwd(), "apk/merged_app.apk")
    }
    options = UiAutomator2Options().load_capabilities(desired_capabilities)
    driver = webdriver.Remote(f'http://localhost:{config.get("ANDROID", "PORT")}', options=options)
    driver.implicitly_wait(20)
    yield driver
    driver.quit()
