#https://rahulshettyacademy.com/dropdownsPractise/
from PracticeEndtoEnd.BaseClass import Baseclass1
from PracticeEndtoEnd.calandersite import Calendar


class TestAutomationGreen(Baseclass1):
    def test_calendar(self):
        self.getlogger()
        obj_cal = Calendar(self.driver)
        obj_cal.cal()
