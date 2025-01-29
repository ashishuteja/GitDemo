#https://rahulshettyacademy.com/AutomationPractice/
from PracticeEndtoEnd.BaseClass import Baseclass1
from PracticeEndtoEnd.automationPractice import Automation



class TestAutomation(Baseclass1):


    def test_automation(self):
        obj_auto = Automation(self.driver)
        #obj_auto.radio()
        #obj_auto.autosuggestdropdown()
        #obj_auto.staticdropdown()
        #obj_auto.checkbox()
        #obj_auto.WindowHandle()

        #obj_auto.Windowhandles()
        #obj_auto.alert()
        #obj_auto.webtable()
        #obj_auto.iframe()
        obj_auto.hover()






