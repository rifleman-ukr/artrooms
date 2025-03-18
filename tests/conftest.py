from pytest import fixture

from pages.art_page import ArtPage
from pages.be_featured_page import BeFeaturedPage
from pages.feedback_page import FeedbackPage
from pages.main_page import MainPage
from pages.menu_page import MenuPage
from pages.rooms_page import RoomsPage
from pages.settings_page import SettingsPage
from pages.subscribe_page import SubscribePage


@fixture(scope="session")
def main_page(driver):
    return MainPage(driver)

@fixture(scope="session")
def menu_page(driver):
    return MenuPage(driver)

@fixture(scope="session")
def settings_page(driver):
    return SettingsPage(driver)

@fixture(scope="session")
def art_page(driver):
    return ArtPage(driver)

@fixture(scope="session")
def subscribe_page(driver):
    return SubscribePage(driver)

@fixture(scope="session")
def be_featured_page(driver):
    return BeFeaturedPage(driver)

@fixture(scope="session")
def rooms_page(driver):
    return RoomsPage(driver)

@fixture(scope="session")
def feedback_page(driver):
    return FeedbackPage(driver)
