import time

from PracticeEndtoEnd.AngularPractice import OneAngular
from PracticeEndtoEnd.BaseClass import Baseclass1
#https://rahulshettyacademy.com/angularpractice

class TestAngular(Baseclass1):

    def test_angular(self):

        self.getlogger()

        obj_angular = OneAngular(self.driver)
        obj_angular.angular()
        obj_angular.dropdown()

        time.sleep(5)

