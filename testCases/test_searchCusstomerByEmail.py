import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByEmail_004(self, setup):
        self.logger.info("*************** SearchCustomerByEmail_004 ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*************** Login successful ***************")

        self.logger.info("*************** Starting Search Customer By Email ***************")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuitem()

        self.logger.info("*************** Searching Customer By Email_ID  ***************")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("brenda_lindgren@nopCommerce.com")
        searchcust.ClickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByEmail("brenda_lindgren@nopCommerce.com")
        assert True == status
        self.logger.info("*************** TC_SearchCustomerByEmail_004 Finished  ***************")
        self.driver.close()
