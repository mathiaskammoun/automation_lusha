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
        welcome_page.open_contact_sales_form()

    def tearDown(self):
        self.driver.quit()


def code():

    # Set Chrome options for headless mode
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")

    # Initialize the Chrome driver with options
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(CONFIG["welcome_page"])

    welcome_page = WelcomePage(driver)
    welcome_page.open_contact_sales_form()



if __name__ == "__main__":
    # unittest.main()

    code()






