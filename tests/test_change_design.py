from utilities.image_utils import compare_screen

def test_change_design(driver, main_page, rooms_page):
    assert main_page.is_page_open(), "Main page should be open"
    assert compare_screen(driver, 'basic_room') > 0.9, "Screen should be same as basic_room.png"
    main_page.open_rooms()
    assert rooms_page.is_page_open(), "Rooms page should be open"
    rooms_page.choose_room()
    assert main_page.is_page_open(), "Main page should be open"
    assert compare_screen(driver, 'changed_room') > 0.9, "Screen should be same as changed_room.png"
