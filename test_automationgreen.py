from PracticeEndtoEnd.BaseClass import Baseclass1
from PracticeEndtoEnd.automationgreenkart import GreenKart


class TestAutomationGreen(Baseclass1):
    def test_geeenkart(self):
        obj_greenkart = GreenKart(self.driver)
        obj_greenkart.greenauto()