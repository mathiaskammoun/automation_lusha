from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver


class WelcomePage(BasePage):

    def is_title_matches(self):
        """Verifies that the hardcoded text "lusha" appears in page title"""
        return "Lusha" in self.driver.title

    def open_contact_sales_form(self):
        """Triggers the search"""
        wait = WebDriverWait(self.driver, 10)

        button_element = wait.until(EC.presence_of_element_located(WelcomePageLocators.CONTACT_SALES_BUTTON))
        # Create an instance of ActionChains
        actions = ActionChains(self.driver)
        # Perform the click action on the button
        actions.double_click(button_element).perform()
        # Wait to make sure the form is opened
        wait.until(EC.visibility_of_element_located(ContactSalesFormLocators.CONTACT_SALES_FORM))


class WelcomePageContactForm(BasePage):

    def is_form_opened(self):
        """ """
        form_element = self.driver.find_element(*ContactSalesFormLocators.CONTACT_SALES_FORM)
        return form_element.is_displayed()

    def fill_form_p1(self, form_p1_keys):
        # form_p1_keys[""]
        Select(self.driver.find_element(*ContactSalesFormLocators.P1_NUMBER_USERS)).select_by_visible_text(form_p1_keys["n_users"])
        Select(self.driver.find_element(*ContactSalesFormLocators.P1_NUMBER_PROSPECTS)).select_by_visible_text(form_p1_keys["n_prospects"])
        Select(self.driver.find_element(*ContactSalesFormLocators.P1_NUMBER_EMPLOYEES)).select_by_visible_text(form_p1_keys["n_employees"])
        Select(self.driver.find_element(*ContactSalesFormLocators.P1_COMPANY_INDUSTRY)).select_by_visible_text(form_p1_keys["industry"])

        self.driver.find_element(*ContactSalesFormLocators.P1_POSITION).send_keys(form_p1_keys["position"])
        self.driver.find_element(*ContactSalesFormLocators.P1_NEXT_BUTTON).click()

    def fill_form_p2(self, form_p2_keys):
        # Wait to make sure the form is opened
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(ContactSalesFormLocators.P2_SUBMIT_BUTTON))

        self.driver.find_element(*ContactSalesFormLocators.P2_FNAME).send_keys(form_p2_keys["fname"])
        self.driver.find_element(*ContactSalesFormLocators.P2_LNAME).send_keys(form_p2_keys["lname"])
        self.driver.find_element(*ContactSalesFormLocators.P2_EMAIL).send_keys(form_p2_keys["email"])
        self.driver.find_element(*ContactSalesFormLocators.P2_PHONE_NUMBER).send_keys(form_p2_keys["phone"])
        self.driver.find_element(*ContactSalesFormLocators.P2_HELP_BOX).send_keys(form_p2_keys["help"])
        time.sleep(3)


class WelcomePageLocators:
    """A class for main page locators. All main page locators should come here"""
    # Locators for contact sales form
    CONTACT_SALES_BUTTON = (By.XPATH, "(//button[contains(@class,'app btn')])[1]")


class ContactSalesFormLocators:

    CONTACT_SALES_FORM = (By.XPATH, "//div[contains(@class,'lusha-popup__container p-0')]")

    P1_NUMBER_USERS = (By.ID, "inputUsers")
    P1_NUMBER_PROSPECTS = (By.ID, "inputAvg")
    P1_NUMBER_EMPLOYEES = (By.ID, "inputEmployees")
    P1_COMPANY_INDUSTRY = (By.ID, "inputIndustry")
    P1_POSITION = (By.ID, "inputPosTxt")
    P1_NEXT_BUTTON = (By.ID, "cf7mls-next-btn-cf7mls_step-1")

    P2_FNAME = (By.ID, "inputFname")
    P2_LNAME = (By.ID, "inputLname")
    P2_EMAIL = (By.ID, "inputEmail")
    P2_PHONE_INDICATOR = ()
    P2_PHONE_NUMBER = (By.ID, "inputPhone")
    P2_HELP_BOX = (By.NAME, "pricing_contact_us_details")
    P2_SUBMIT_BUTTON = (By.XPATH, "//input[contains(@class,'wpcf7-form-control wpcf7-submit')]")


