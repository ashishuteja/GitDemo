#https://rahulshettyacademy.com/dropdownsPractise/
import time

from select import select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PracticeEndtoEnd.conftest import driver


#https://rahulshettyacademy.com/seleniumPractise


class Calendar:
    def __init__(self, driver):
        self.driver = driver

    def cal(self):

        self.driver.find_element(By.ID,"ctl00_mainContent_rbtnl_Trip_1").click()
        self.driver.find_element(By.ID,"ctl00_mainContent_ddl_originStation1_CTXT").click()
        self.driver.find_element(By.XPATH,"(//div[@class='dropdownDiv'])[1]/ul[1]/li[5]/a").click()
        self.driver.find_element(By.XPATH,"(//div[@class='dropdownDiv'])[3]/ul[2]/li[2]").click()
        self.driver.find_element(By.ID,"ctl00_mainContent_view_date1").click()
        self.driver.find_element(By.XPATH,"(//table[@class='ui-datepicker-calendar'])[1]/tbody/tr[4]/td[5]/a").click()
        self.driver.find_element(By.ID,"divpaxinfo").click()
        self.driver.find_element(By.XPATH,"(//span[@class='pax-add pax-enabled'])[1]").click()
        self.driver.find_element(By.XPATH,"(//input[@class='buttonN'])[1]").click()
        self.driver.find_element(By.LINK_TEXT,"Special Assistance").click()
        self.driver.find_element(By.XPATH,"(//a[@class='pdf-download-icon'])[1]").click()
        obj_windowhandle = driver.window_handles
        driver.switch_to.window(obj_windowhandle[0])
        self.driver.find_element(By.XPATH,"//a[@class='popup-close2']").click()
        obj_mousehover = self.driver.find_element(By.ID,"ctl00_mainContent_IndArm")
        obj_actions = ActionChains(driver)
        obj_actions.move_to_element(obj_mousehover).perform()

        time.sleep(10)