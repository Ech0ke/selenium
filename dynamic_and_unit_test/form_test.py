import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Drivers\chromedriver\chromedriver.exe"


class TestHtmlForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(PATH)

    def test_registration_form_1(self):
        """
        Test that form is submitted successfully
        """

        self.driver.get("http://suninjuly.github.io/registration1.html")

        # Field values
        person_info = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "example@gmail.com",
            "phone": "+442071234567",
            "address": "Maple Street 1, London, England"
        }

        # Find input fields
        first_name_input = self.driver.find_element_by_xpath(
            "//label[contains(text(),'First name')]/following-sibling::input")
        last_name_input = self.driver.find_element_by_xpath(
            "//label[contains(text(),'Last name')]/following-sibling::input")
        email_input = self.driver.find_element_by_xpath(
            "//label[contains(text(),'Email')]/following-sibling::input")
        phone_input = self.driver.find_element_by_xpath(
            "//label[contains(text(),'Phone')]/following-sibling::input")
        address_input = self.driver.find_element_by_xpath(
            "//label[contains(text(),'Address')]/following-sibling::input")

        # Find submit button
        submit_button = self.driver.find_element_by_css_selector(
            "button[type='submit']")

        # Type person info into input fields
        first_name_input.send_keys(person_info["first_name"])
        last_name_input.send_keys(person_info["last_name"])
        email_input.send_keys(person_info["email"])
        phone_input.send_keys(person_info["phone"])
        address_input.send_keys(person_info["address"])

        # Submit form
        submit_button.click()

        # Assert that submission was successful
        success_message = self.driver.find_element_by_css_selector(
            "div.container > h1")
        self.assertEqual(success_message.text,
                         "Congratulations! You have successfully registered!")

    def test_registration_form_2(self):
        """
        Test that form is submitted successfully
        """

        self.driver.get("http://suninjuly.github.io/registration2.html")

        # Field values
        person_info = {
            "first_name": "John",
        }

        # Find input fields
        first_name_input = self.driver.find_element_by_xpath(
            "//label[contains(text(),'First name')]/following-sibling::input")

        # Find submit button
        submit_button = self.driver.find_element_by_css_selector(
            "button[type='submit']")

        # Type person info into input fields
        first_name_input.send_keys(person_info["first_name"])

        # Submit form
        submit_button.click()

        # Assert that submission was successful
        success_message = self.driver.find_element_by_css_selector(
            "div.container > h1")
        self.assertEqual(success_message.text,
                         "Congratulations! You have successfully registered!")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
