from utilities.config import config

def test_rooms_filter(driver, main_page, rooms_page):
    assert main_page.is_page_open(), "Main page should be open"
    main_page.open_rooms()
    assert rooms_page.is_page_open(), "Rooms page should be open"
    rooms_page.apply_filter(config.get("TEST_DATA", "FILTER"))
    assert rooms_page.get_filter_button_text() == config.get("TEST_DATA", "FILTER"), \
        "Applied filter should be displayed"
    rooms_page.go_back()

def test_rooms_import(driver, main_page, rooms_page, subscribe_page):
    assert main_page.is_page_open(), "Main page should be open"
    main_page.open_rooms()
    assert rooms_page.is_page_open(), "Rooms page should be open"
    rooms_page.click_import()
    assert subscribe_page.is_page_open(), "Subscribe page should be open"
    subscribe_page.go_back()
    rooms_page.go_back()