from selenium.webdriver.common.by import By


class WelcomePage:

    def __init__(self, driver):
        self.driver = driver

    def is_title_matches(self):
        """Verifies that the hardcoded text "lusha" appears in page title"""

        return "Lusha" in self.driver.title

    def click_form_button(self):
        """Triggers the search"""

        element = self.driver.find_element(*WelcomePageLocators.CONTACT_SALES_BUTTON)
        element.click()


class WelcomePageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    # CONTACT_SALES_BUTTON = (By.CLASS_NAME, "app btn js-contact-form-btn contact-sales-btn d-lo d-li-none m-0")
    # CONTACT_SALES_BUTTON = (By.CLASS_NAME, "app contact-sales js-contact-form-btn btn d-li d-lo-none animate__fadeIn animate__animated animate__faster")
    CONTACT_SALES_BUTTON = (By.ID, 'header-form-contact-sales-visitors-button')