from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_button_buy(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#add_to_basket_form > button")