def test_change_units(driver, main_page, menu_page, settings_page):
    assert main_page.is_page_open(), "Main page should be open"
    main_page.open_menu()
    assert menu_page.is_page_open(), "Menu page should be open"
    menu_page.open_settings()
    assert settings_page.is_page_open(), "Settings page should be open"
    if not settings_page.are_units_metric():
        settings_page.change_units()
        assert settings_page.are_units_metric(), "Units should be metric"
    settings_page.return_to_main_page()

def test_check_units_in_arts(driver, main_page, art_page):
    assert main_page.is_page_open(), "Main page should be open"
    main_page.open_art()
    assert art_page.is_page_open(), "Art page should be open"
    assert art_page.are_units_metric(), "Units should be metric"
    art_page.return_to_main_page()
