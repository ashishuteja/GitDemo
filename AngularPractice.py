import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


#https://rahulshettyacademy.com/angularpractice

class OneAngular:

    def __init__(self, driver):
        self.driver = driver

    def angular(self):
        self.driver.find_element(By.LINK_TEXT,"Shop").click()
        names = self.driver.find_elements(By.XPATH,"//h4[@class='card-title']")
        #print(names.text)

        for name in names:
            print(name.text)

        buttons = self.driver.find_elements(By.XPATH,"//button[@class='btn btn-info']")
        for button in buttons:
            if button.get_attribute("class") == "btn btn-info":
                button.click()

    def dropdown(self):
        self.driver.find_element(By.XPATH,"//div[@class='container']/a[1]").click()
        self.driver.find_element(By.XPATH,"(//input[@name='name'])[1]").send_keys("test")
        self.driver.find_element(By.XPATH, "(//input[@name='email'])[1]").send_keys("test@gmail.com")
        drpdwn = Select(self.driver.find_element(By.ID,"exampleFormControlSelect1"))
        drpdwn.select_by_index(1)
        self.driver.find_element(By.XPATH,"//input[@type='submit']").click()
        time.sleep(8)
        element = self.driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
        assert "Success! The Form has been submitted successfully!." in element
        #return print(element.text)
        #assert element.text == "Success! The Form has been submitted successfully!."

