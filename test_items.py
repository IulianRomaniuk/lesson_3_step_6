import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"

class Test_basket(): 
    def test_basket_button(self):
        driver = webdriver.Chrome()
        driver.get(link)
        driver.execute_script("window.scrollTo(0, 540)")
        
        assert driver.find_element_by_xpath("//button[@value='Add to basket']")