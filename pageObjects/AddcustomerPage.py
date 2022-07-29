import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver


class AddCustomer:
    # Add customer Page
    linkCustomer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    linkCustomer_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')] "
    btnAddnew_xpath = "//a[normalize-space()='Add new']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    checkBoxIsTaxExempt_xpath = "//input[@id='IsTaxExempt']"
    txtCustomerRole_index_xpath = "//div[@role='listbox']"
    lstAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemForumModerators_xpath = "//li[contains(text(),'Forum Moderators')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemVendor_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrOfVendor_xpath = "//select[@id='VendorId']"
    checkBoxActive_xpath = "//input[@id='Active']"
    txtAddminComment_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.linkCustomer_menu_xpath).click()

    def clickOnCustomersMenuitem(self):
        self.driver.find_element(By.XPATH, self.linkCustomer_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()

    def setDOB(self, dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setCompany(self, company):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(company)

    def checkboxIsTaxExempt(self):
        self.driver.find_element(By.XPATH, self.checkBoxIsTaxExempt_xpath).click()

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txtCustomerRole_index_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstAdministrators_xpath)
        elif role == 'Forum Moderators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemForumModerators_xpath)
        elif role == 'Guests':
            # Here user can be Registered (or) Guest, only one
            time.sleep(3)
            self.driver.find_element(By.XPATH, "(//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2])").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstAdministrators_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendor_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def clickOncheckBoxActive(self):
        self.driver.find_element(By.XPATH, self.clickOncheckBoxActive).click()

    def setAdminComment(self, value):
        self.driver.find_element(By.XPATH, self.txtAddminComment_xpath).send_keys(value)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()
