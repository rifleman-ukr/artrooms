from utilities.config import config

def test_subscribe_button(driver, main_page, menu_page, subscribe_page):
    assert main_page.is_page_open(), "Main page should be open"
    main_page.open_menu()
    assert menu_page.is_page_open(), "Menu page should be open"
    menu_page.open_subscribe_page()
    assert subscribe_page.is_page_open(), "Subscribe page should be open"
    subscribe_page.go_back()

def test_feedback_button(driver, menu_page, feedback_page):
    assert menu_page.is_page_open(), "Menu page should be open"
    menu_page.open_feedback_form()
    assert feedback_page.is_page_open(), "Feedback form page should be open"
    feedback_page.send_feedback(config.get("TEST_DATA", "NAME"), config.get("TEST_DATA", "TEXT"))
    assert feedback_page.is_android_content_panel_displayed(), "Android sharing panel should be displayed"
    feedback_page.system_back()

def test_be_featured_button(driver, menu_page, be_featured_page):
    assert menu_page.is_page_open(), "Menu page should be open"
    menu_page.open_be_featured_form()
    assert be_featured_page.is_page_open(), "Featured page should be open"
    be_featured_page.submit_form(config.get("TEST_DATA", "TEXT"))
    assert be_featured_page.is_android_content_panel_displayed(), "Android sharing panel should be displayed"
    be_featured_page.system_back()

def test_invite_page(driver, menu_page):
    assert menu_page.is_page_open(), "Menu page should be open"
    menu_page.open_invite_page()
    assert menu_page.is_android_content_panel_displayed(), "Android sharing panel should be displayed"
    menu_page.system_back()
    menu_page.go_back()
