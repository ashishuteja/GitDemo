import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Baseclasss import Basecls
from PageObjects.HomePage import HomePage


class TestOne(Basecls):

    def test_e2ee(self, getdata1):

        homepage = HomePage(self.driver)
        homepage.getname().send_keys(getdata1["Name"])
        homepage.getemail().send_keys(getdata1["EmilId"])
        homepage.selcheck().click()
        #self.seldropdown(homepage.getgender(),"Male")----check again this, its coming from baseclass
        homepage.getsubmitbutton().click()
        homepage.shopItems().click()
        #self.verifylinkpresence("India")
        #self.driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
        self.driver.refresh()

    @pytest.fixture(params=[{"Name":"ASHISH TUTEJA", "EmilId":"@gmail.com"}])
    def getdata1(self, request):
        return request.param