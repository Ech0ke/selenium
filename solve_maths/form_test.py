import re
import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Drivers\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

EQUATION_PATTERN = r'\bln\(abs\(12\*sin\(x\)\)\)'


def reformat_equation(math_equation, x_value):
    math_equation = math_equation.replace("x", x_value)
    math_equation = math_equation.replace("ln", "math.log")
    math_equation = math_equation.replace("sin", "math.sin")
    return math_equation


# Load the website
driver.get("https://suninjuly.github.io/alert_accept.html")

# Find accept button
accept_button = driver.find_element_by_css_selector("button[type='submit']")

# Click accept button
accept_button.click()

# Accept pop-up alert
alert = driver.switch_to.alert
alert.accept()

# Wait for redirected page to load
WebDriverWait(driver, 10).until(EC.url_changes)

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
