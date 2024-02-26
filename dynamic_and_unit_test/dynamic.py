import re
import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

PATH = "C:\Drivers\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

EQUATION_PATTERN = r'\bln\(abs\(12\*sin\(x\)\)\)'

# Load the website
driver.get("http://suninjuly.github.io/explicit_wait2.html")

# Find house price
driver.find_element_by_css_selector("#price")

# Find book button
book_button = driver.find_element_by_css_selector("#book")


def reformat_equation(math_equation, x_value):
    math_equation = math_equation.replace("x", x_value)
    math_equation = math_equation.replace("ln", "math.log")
    math_equation = math_equation.replace("sin", "math.sin")
    return math_equation

# Check if price of the house is $100


def wait_for_value_100(driver):
    price = driver.find_element_by_css_selector("#price")
    return price.text == "$100"


# Try to get best price ($100), or timeout and exit
try:
    WebDriverWait(driver, 15).until(wait_for_value_100)
except TimeoutException:
    print("Timed out waiting for the value to become 100")
    driver.quit()
    quit()

# Click Book button
book_button.click()

# Get math equation sentence
math_equation_sentence = driver.find_element_by_css_selector(
    "div.form-group > label > span:first-child").text

# Extract only the equation
math_equation = re.search(EQUATION_PATTERN, math_equation_sentence).group()

# Get value of x needed to solve the equation
x_value = driver.find_element_by_css_selector("#input_value").text

# Perform some equation parts reformatting in order to pass it to eval later
reformatted_math_equation = reformat_equation(math_equation, x_value)

result = eval(reformatted_math_equation)

# Get equation answer field
result_input_field = driver.find_element_by_css_selector("#answer")

# Type answer into the field as string
result_input_field.send_keys(str(result))

# Submit answer
submit_button = driver.find_element_by_css_selector("button[type='submit']")
submit_button.click()

# Print success message
alert = driver.switch_to.alert
print(alert.text)

driver.quit()
