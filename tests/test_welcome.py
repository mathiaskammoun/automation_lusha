from os.path import dirname
import json

from selenium import webdriver

import unittest

from pages.welcome_page import WelcomePage, WelcomePageContactForm

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

        contact_form = WelcomePageContactForm(self.driver)
        # Checks if the form opened
        self.assertTrue(contact_form.is_form_opened())

        form_p1_keys = {"n_users": "1-5", "n_prospects": "400-1000",
                        "n_employees": "201-500", "industry": "Industrials", "position": "Sales"}
        contact_form.fill_form_p1(form_p1_keys)

        form_p2_keys = {"fname": "Mickey", "lname": "Mouse", "email": "m_mouse@gmail.com",
                        "phone": "343-245-3453", "help": "Thank You!"}
        contact_form.fill_form_p2(form_p2_keys)


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
    contact_form = WelcomePageContactForm(driver)
    assert contact_form.is_form_opened()

    form_p1_keys = {"n_users": "1-5", "n_prospects": "400-1000",
                    "n_employees": "201-500", "industry": "Industrials", "position": "Sales"}
    contact_form.fill_form_p1(form_p1_keys)

    form_p2_keys = {"fname": "Mickey", "lname": "Mouse", "email": "m_mouse@gmail.com",
                    "phone": "343-245-3453", "help": "Thank You!"}
    contact_form.fill_form_p2(form_p2_keys)


if __name__ == "__main__":
    # unittest.main()

    code()






