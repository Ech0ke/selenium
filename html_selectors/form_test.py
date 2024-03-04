from selenium import webdriver
import time
PATH = "C:\Drivers\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Load the website
driver.get("http://suninjuly.github.io/simple_form_find_task.html")

# Field values
person_info = {
    "first_name": "John",
    "last_name": "Doe",
    "city": "New York",
    "country": "United States",
}

# Find input fields
first_name_input = driver.find_element_by_xpath(
    "//label[contains(text(),'First name')]/following-sibling::input")
last_name_input = driver.find_element_by_xpath(
    "//label[contains(text(),'Last name')]/following-sibling::input")
city_input = driver.find_element_by_xpath(
    "//label[contains(text(),'City')]/following-sibling::input")
country_input = driver.find_element_by_xpath(
    "//label[contains(text(),'Country')]/following-sibling::input")

# Find submit button
submit_button = driver.find_element_by_css_selector(
    "button[type='submit']")

# Type person info into input fields
first_name_input.send_keys(person_info["first_name"])
last_name_input.send_keys(person_info["last_name"])
city_input.send_keys(person_info["city"])
country_input.send_keys(person_info["country"])

submit_button.click()

# Print alerted message
alert = driver.switch_to.alert
print(alert.text)

driver.quit()
