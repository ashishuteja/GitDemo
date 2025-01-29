import time

from select import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


#https://rahulshettyacademy.com/seleniumPractise


class GreenKart:
    def __init__(self, driver):
        self.driver = driver

    def greenauto(self):
        self.driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("er")
        time.sleep(5)
        buttons = self.driver.find_elements(By.XPATH,"//div[@class='product-action']/button")
        for button in buttons:
            button.click()
        names = self.driver.find_elements(By.XPATH,"//h4[@class='product-name']")
        for name in names:
            print(name.text)
        self.driver.find_element(By.CSS_SELECTOR,".cart-icon").click()
        self.driver.find_element(By.XPATH,"(//button[@type='button'])[1]").click()
        time.sleep(5)
        prices = self.driver.find_elements(By.XPATH,"//div[@class='products']/table/tbody/tr/td[5]/p")
        sum = 0
        for price in prices:
            sum = sum + int(price.text)
            print(price.text)
        print(sum)
        if sum >100:
            print("Test caes is passed")
        else:
            print("Test case is failed")

        self.driver.find_element(By.XPATH,"//button[contains(text(),'Place Order')]").click()
        elements = Select(self.driver.find_element(By.XPATH,"//div[@class='wrapperTwo']/div/select"))
        elements.select_by_visible_text("Angola")
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
        self.driver.find_element(By.XPATH,"//button[contains(text(),'Proceed')]").click()
        time.sleep(10)

        buttonss = self.driver.find_elements(By.XPATH,"//button[contains(text(),'ADD TO CART')]")
        for buttonn in buttonss:
            buttonn.click()

        #assert sum == (By.XPATH,"//span[@class='totAmt']").text()
