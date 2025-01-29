import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)


@pytest.fixture(scope="class")
def setup1(request):
    driver.implicitly_wait(10)
    #driver.get("https://rahulshettyacademy.com/angularpractice")
    #driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    #driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

    driver.maximize_window()
    request.cls.driver = driver
    yield





