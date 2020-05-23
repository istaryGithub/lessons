import pytest, time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

def test_link(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	browser.get(link)
	browser.implicitly_wait(6)
	add_button = browser.find_element_by_id('add_to_basket_form')
	assert add_button, "Button wasn't found"
	time.sleep(4)
