import time
#https://rahulshettyacademy.com/angularpractice
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from tests.conftest import driver
class Practice:
    def __init__(self, driver):
        self.driver = driver

    #name = (By.CSS_SELECTOR,"input[name ='name']")


    def getlogin(self):
        #return driver.find_element(*Practice.name)
        driver.find_element(By.CSS_SELECTOR,"input[name ='name']").send_keys("Ashisssssssssssssssh")
        driver.find_element(By.XPATH,"//input[@name='email']").send_keys("ashish@gmail.com")
        driver.find_element(By.ID,"exampleInputPassword1").send_keys("ashish@")
        driver.find_element(By.ID,"exampleCheck1").click()
        driver.find_element(By.XPATH,"//form/div[4]/input").click()#this locator of checkbox issue-on chropath it works
        driver.find_element(By.ID,"exampleCheck1").click()
        time.sleep(4)

    def getselectdropdown(self):
        dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
        dropdown.select_by_visible_text("Female")
        driver.find_element(By.XPATH,"//input[@type='submit']").click()



