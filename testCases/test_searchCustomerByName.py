import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_005_searchCustomerByName(self, setup):
        self.logger.info("*************** test_005_searchCustomerByName ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*************** Login successful ***************")

        self.logger.info("*************** Starting Search Customer By Name ***************")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuitem()

        self.logger.info("*************** Searching Customer By Name  ***************")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Brenda")
        searchcust.setLastName("Lindgren")
        searchcust.ClickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByName("Brenda Lindgren")
        assert True == status
        self.logger.info("*************** test_005_searchCustomerByName Finished  ***************")
        self.driver.close()
