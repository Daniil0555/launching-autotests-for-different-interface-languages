import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_shopping_cart(browser):
    browser.get(link)
    # time.sleep(30) # Поможет при проверке языка на странице
    button = browser.find_elements_by_class_name("btn-add-to-basket")
    assert button, "Not found button"
