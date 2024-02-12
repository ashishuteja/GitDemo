from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver


    Name = (By.XPATH,"//body/app-root[1]/form-comp[1]/div[1]/form[1]/div[1]/input[1]")
    Email = (By.XPATH,"//body/app-root[1]/form-comp[1]/div[1]/form[1]/div[2]/input[1]")
    Passwrd = (By.XPATH,"//input[@id='exampleInputPassword1']")
    checkbox = (By.XPATH,"//input[@id='exampleCheck1']")
    submitbtn = (By.XPATH,"//body/app-root[1]/form-comp[1]/div[1]/form[1]/input[1]")
    shop = (By.CSS_SELECTOR,"a[href*='shop']")
    gender = (By.ID,"exampleFormControlSelect1")

    def getname(self):
        return self.driver.find_element(*HomePage.Name)
    def getemail(self):
        return self.driver.find_element(*HomePage.Email)
    def selcheck(self):
        return self.driver.find_element(*HomePage.checkbox)
    def getsubmitbutton(self):
        return self.driver.find_element(*HomePage.submitbtn)
    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)
    def getgender(self):
        return self.driver.find_element(HomePage.gender)


