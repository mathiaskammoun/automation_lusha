from os.path import dirname
import json

from selenium import webdriver

import unittest

from pages.welcome_page import WelcomePage

with open(dirname(__file__) + "/../config.json", "r") as jsonfile:
    CONFIG = json.load(jsonfile)


class Lusha_ContactSales(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(CONFIG["welcome_page"])

    def test_contactSalesForm(self):
        """
        Test lusha.com contact sales feature
        :return:
        """
        # Load the main page. In this case the home page of Python.org.
        welcome_page = WelcomePage(self.driver)
        # Checks if the word "Python" is in title
        self.assertTrue(welcome_page.is_title_matches(), "Lusha title doesn't match.")
        welcome_page.click_form_button()

    def tearDown(self):
        self.driver.quit()


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def code():

    # Set Chrome options for headless mode
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")

    # Initialize the Chrome driver with options
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(CONFIG["welcome_page"])

    welcome_page = WelcomePage(driver)

    # tags = (By.CLASS_NAME, "app.btn.js-contact-form-btn.contact-sales-btn.d-lo.d-li-none.m-0")
    tags = (By.XPATH, "//button[contains(@class, 'app btn js-contact-form-btn contact-sales-btn d-lo d-li-none m-0') and @data-test-id='header-form-contact-sales-visitors-button']")

    # button_element = driver.find_element(*tags)
    button_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(tags))
    button_element.click()

    wait = WebDriverWait(driver, 10)
    form_element = wait.until(EC.presence_of_element_located((By.ID, "cf7mls-next-btn-cf7mls_step-1")))

    # Check if the form is displayed
    if form_element.is_displayed():
        print("The form is open.")
    else:
        print("The form did not open as expected.")


if __name__ == "__main__":
    # unittest.main()

    code()






