import time
#use below website for autosuggestive dropdown in conftest file.

#dynamic checkbox, alert popup           #https://rahulshettyacademy.com/dropdownsPractise/
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from tests.conftest import driver
class Autoselectcheckbox:
    def __init__(self, driver):
        self.driver = driver

    def getautoselectchkbox(self):
        checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
        for checkbox in checkboxes:
            if checkbox.get_attribute("value") == "ctl00_mainContent_chk_SeniorCitizenDiscount":
                checkbox.click()
                break

    def getradiobutton(self):
        radiobuttons = driver.find_elements(By.XPATH,"//input[@type='radio']")
        for radiobutton in radiobuttons:
            if radiobutton.get_attribute(("value"))=="radio3":
                radiobutton.click()
                assert radiobutton.is_selected()
                break

    def getradiobutton1(self):#through indexing number, like it will be clicked on 2nd always.
        radiobuttons1 = driver.find_elements(By.XPATH,"//input[@type='radio']")
        radiobuttons1[0].click()
        assert radiobuttons1[0].is_selected()

    def getalert(self):
        driver.find_element(By.XPATH,"//input[@id='alertbtn']").click()
        alert = driver.switch_to.alert
        print(alert.text)
        alert.accept() #alert.dismiss()
        