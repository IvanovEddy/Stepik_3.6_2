import time


def test_guest_button_language(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = lambda: browser.find_element_by_css_selector(".btn-add-to-basket")
    assert button() is not None
    time.sleep(30)
