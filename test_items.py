link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_find_button(browser):
    browser.get(link)
    button = browser.find_elements_by_css_selector(".btn-primary")
    assert button, "Button Add to basket not found"