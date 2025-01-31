import time
##explicit wait
from selenium.webdriver.chrome.webdriver import WebDriver
#use below website for waits in conftest file.
#https://rahulshettyacademy.com/seleniumPractise/#/

#dynamic checkbox, alert popup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.conftest import driver

class Waitss:
    def __init__(self, driver):
        self.driver = driver

    def getwait(self):
        driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")
        driver.find_element(By.XPATH,"//button[@class='search-button']").click()
        time.sleep(3)




        counts = driver.find_elements(By.XPATH,"//div[@class='products']/div/div[3]/button")

        for count in counts:
            count.click()
        driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
        driver.find_element(By.XPATH,"//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
        driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshetty")
        driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
        #wait1 = WebDriverWait(driver, 20)
        #wait1.until(expected_conditions.presence_of_element_located(By.CLASS_NAME, "promoInfo"))
        #print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)
        prices = driver.find_elements(By.XPATH,"//tr/td[5]/p")
        sum = 0
        for price in prices:
            sum = sum + int(price.text)
        print(sum)
        totalamount = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
        assert sum == totalamount


