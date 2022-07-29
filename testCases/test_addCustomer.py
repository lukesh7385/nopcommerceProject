import string
import random
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("*************** Test_003_AddCustomer ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*************** Login successful ***************")

        self.logger.info("*************** Starting Add Customer Test ***************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuitem()

        self.addcust.clickOnAddnew()

        self.logger.info("*************** Providing customer info ***************")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setFirstName("Lukesh")
        self.addcust.setLastName("Ade")
        self.addcust.setGender("Male")
        self.addcust.setDOB("10/13/9094")
        self.addcust.setCompany("HCL")
        self.addcust.checkboxIsTaxExempt()
        self.addcust.setAdminComment("This is for testing.....................")
        self.addcust.clickOnSave()

        self.logger.info("*************** Saving customer info ***************")

        self.logger.info("*************** Add customer validation started ***************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        if 'The new customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("*************** Add customer test pass ***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("*************** Add customer Test Failed ***************")
            assert True == False

        self.driver.close()
        self.logger.info("*************** Ending Add Customer Test ***************")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
