import time
from selenium.webdriver.common.by import By


class SearchCustomer:
    txtEmail_id = "SearchEmail"
    txtFirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"
    Table_xpath = "//table[@id='customers-grid']"
    Table_rows_xpath = "//table[@id='customers-grid']/tbody/tr"
    Table_column_xpath = "//table[@id='customers-grid']/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txtEmail_id).clear()
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def setFirstName(self, firstname):
        self.driver.find_element(By.ID, self.txtFirstName_id).clear()
        self.driver.find_element(By.ID, self.txtFirstName_id).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.ID, self.txtLastName_id).clear()
        self.driver.find_element(By.ID, self.txtLastName_id).send_keys(lastname)

    def ClickSearch(self):
        self.driver.find_element(By.ID, self.btnSearch_id).click()

    def getNoOfRow(self):
        return len(self.driver.find_elements(By.XPATH, self.Table_rows_xpath))

    def getNoOfColumn(self):
        return len(self.driver.find_element(By.XPATH, self.Table_column_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRow() + 1):
            table = self.driver.find_element(By.XPATH, self.Table_xpath)
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, name):
        flag = False
        for r in range(1, self.getNoOfRow() + 1):
            table = self.driver.find_element(By.XPATH, self.Table_xpath)
            Nameid = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
            if Nameid == name:
                flag = True
                break
        return flag
