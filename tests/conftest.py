import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service()
driver = webdriver.Chrome(service= service_obj)



@pytest.fixture(scope="class")
def setup(request):
    driver.get("https://rahulshettyacademy.com/angularpractice")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    time.sleep(10)
    driver.close()

@pytest.fixture(params=[("chrome", "Ashish","ashish@gmail.com")])
def crossbrowser(request):
    return request.param






