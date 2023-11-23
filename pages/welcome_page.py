from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


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

        form_element = wait.until(EC.presence_of_element_located(ContactSalesFormLocators.CONTACT_SALES_FORM))
        print(form_element.is_displayed())


class WelcomePageLocators:
    """A class for main page locators. All main page locators should come here"""
    # Locators for contact sales form
    CONTACT_SALES_BUTTON = (By.XPATH, "(//button[contains(@class,'app btn')])[1]")


class ContactSalesFormLocators:

    # CONTACT_SALES_FORM = (By.ID, "cf7mls-next-btn-cf7mls_step-1")
    CONTACT_SALES_FORM = (By.XPATH, "//div[contains(@class,'lusha-popup__container p-0')]")
