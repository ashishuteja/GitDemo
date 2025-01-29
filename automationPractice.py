import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common import alert, actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PracticeEndtoEnd.conftest import driver


#https://rahulshettyacademy.com/AutomationPractice/
class Automation:

    def __init__(self, driver):
        self.driver = driver


    def radio(self):
        radiobuttons = self.driver.find_elements(By.XPATH,"(//div[@class='left-align'])[1]/fieldset/label/input")
        for radiobutton in radiobuttons:
            if radiobutton.get_attribute("value") == "radio2":
                radiobutton.click()


    #autosuggest dropdown

    def autosuggestdropdown(self):
        self.driver.find_element(By.XPATH,"//input[@id='autocomplete']").send_keys("ind")
        elements = self.driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']/div")
        for element in elements:
            if element.text =="India":
                element.click()

    #dropdown
    def staticdropdown(self):
        dropdown = Select(self.driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']"))
        dropdown.select_by_visible_text("Option2")
        time.sleep(5)


#checkbox
    def checkbox(self):
        checkboxes = self.driver.find_elements(By.XPATH,"//div[@id='checkbox-example']/fieldset/label/input")
        for checkbox in checkboxes:
            checkbox.click()

#windowHandles
    def WindowHandle(self):
        self.driver.find_element(By.XPATH,"//button[@id='openwindow']").click()
        obj_window = self.driver.window_handles
        self.driver.switch_to.window(obj_window[1])
        self.driver.find_element(By.LINK_TEXT,"Courses").click()
        driver.close()





    def Windowhandles(self):
        obj_window = driver.window_handles
        self.driver.switch_to.window(obj_window[0])

        self.driver.find_element(By.XPATH,"//a[@id='opentab']").click()

        obj_window = driver.window_handles
        self.driver.switch_to.window(obj_window[1])
        time.sleep(10)
        self.driver.find_element(By.XPATH,"(//a[@class='main-btn'])[1]").click()
        self.driver.switch_to.window(obj_window[0])

        time.sleep(10)

    def alert(self):
        self.driver.find_element(By.ID,"alertbtn").click()
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.accept()
        self.driver.find_element(By.ID,"confirmbtn").click()
        alert1 = self.driver.switch_to.alert
        print(alert1.text)
        alert1.dismiss()

    def webtable(self):
        webelements = self.driver.find_elements(By.XPATH,"(//table[@id='product'])[1]/tbody/tr/td[2]")
        for webelement in webelements:
            print(webelement.text)
        prices = self.driver.find_elements(By.XPATH,"(//table[@id='product'])[1]/tbody/tr/td[3]")
        sum = 0
        for price in prices:
            sum = sum + int(price.text)
        print(sum)
        #print(price.text)

    def iframe(self):
        obj_frame = self.driver.find_element(By.ID,"courses-iframe")
        driver.switch_to.frame(obj_frame)
        self.driver.find_element(By.XPATH,"(//a[@class='theme-btn'])[1]").click()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID,"hide-textbox").click()
        time.sleep(5)

    def hover(self):
        obj_mousehover = self.driver.find_element(By.ID,"mousehover")
        obj_actions = ActionChains(driver)
        obj_actions.move_to_element(obj_mousehover).perform()
        time.sleep(10)
        obj_clicks = driver.find_element(By.LINK_TEXT, "Reload")
        obj_actions.move_to_element(obj_mousehover).click(obj_clicks).perform()
        time.sleep(10)






