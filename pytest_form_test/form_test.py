import pytest
from selenium import webdriver


PATH = "C:\Drivers\chromedriver\chromedriver.exe"


@pytest.fixture()
def browser():
    # Initialize browser instance
    driver = webdriver.Chrome(PATH)

    # Provide driver to test function for use
    yield driver

    # After test completes, quit browser session
    driver.quit()


class TestHtmlForm():
    def test_registration_form_1(self, browser):
        """
        Test that form is submitted successfully
        """

        browser.get("http://suninjuly.github.io/registration1.html")

        # Field values
        person_info = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "example@gmail.com",
            "phone": "+442071234567",
            "address": "Maple Street 1, London, England"
        }

        # Find input fields
        first_name_input = browser.find_element_by_xpath(
            "//label[contains(text(),'First name')]/following-sibling::input")
        last_name_input = browser.find_element_by_xpath(
            "//label[contains(text(),'Last name')]/following-sibling::input")
        email_input = browser.find_element_by_xpath(
            "//label[contains(text(),'Email')]/following-sibling::input")
        phone_input = browser.find_element_by_xpath(
            "//label[contains(text(),'Phone')]/following-sibling::input")
        address_input = browser.find_element_by_xpath(
            "//label[contains(text(),'Address')]/following-sibling::input")

        # Find submit button
        submit_button = browser.find_element_by_css_selector(
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
        success_message = browser.find_element_by_css_selector(
            "div.container > h1")

        assert success_message.text == "Congratulations! You have successfully registered!"

    def test_registration_form_2(self, browser):
        """
        Test that form is submitted successfully
        """

        browser.get("http://suninjuly.github.io/registration2.html")

        # Field values
        person_info = {
            "first_name": "John",
        }

        # Find input fields
        first_name_input = browser.find_element_by_xpath(
            "//label[contains(text(),'First name')]/following-sibling::input")

        # Find submit button
        submit_button = browser.find_element_by_css_selector(
            "button[type='submit']")

        # Type person info into input fields
        first_name_input.send_keys(person_info["first_name"])

        # Submit form
        submit_button.click()

        # Assert that submission was successful
        success_message = browser.find_element_by_css_selector(
            "div.container > h1")

        assert success_message.text == "Congratulations! You have successfully registered!"
