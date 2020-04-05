import pytest
from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_item_add_to_basket(browser):
    browser.get(link)
    time.sleep(7)
    assert browser.find_element_by_css_selector("button.btn-add-to-basket")