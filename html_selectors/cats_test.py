from selenium import webdriver
PATH = "C:\Drivers\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://suninjuly.github.io/cats.html")

# Get title of the page by CSS selector
webpage_title = driver.find_element_by_css_selector(
    "main section.jumbotron.text-center div.container h1.jumbotron-heading")

first_button = driver.find_element_by_css_selector("[type='button']")

# Get first cat image by id
first_cat_image_by_id = driver.find_element_by_id("bullet")
first_cat_image_by_selector = driver.find_element_by_css_selector("#bullet")

# Get cat by data-name property
politic_cat = driver.find_element_by_name("Vova")

# Get all cat meme descriptions
all_cat_descriptions = driver.find_elements_by_class_name("card-text")

fourth_cat_minutes_by_xpath = driver.find_element_by_xpath(
    "/html/body/main/div/div/div/div[3]/div/div/div/small")

moto = driver.find_element_by_xpath("//article[@id='moto']")
# Print the results
print("Found elements:\n--------------------------------------")
print(f"Heading of the page - {webpage_title.text}")
print(f"First found button text - {first_button.text}")
print(
    f"First cat image found by id:\n\tImage URL - {first_cat_image_by_id.get_attribute('src')}\n\tAlt text: - {first_cat_image_by_id.get_attribute('alt')}\n\tLocation: - {first_cat_image_by_id.location}")
print(
    f"First cat image found by id css selector:\n\tImage URL - {first_cat_image_by_selector.get_attribute('src')}\n\tAlt text: - {first_cat_image_by_selector.get_attribute('alt')}\n\tLocation: - {first_cat_image_by_selector.location}")
print(f"Politic cat - {politic_cat.text}")
print("All cat meme descriptions:")
for x in range(len(all_cat_descriptions)):
    print(f"\t {all_cat_descriptions[x].text}")
print(f"Cat minutes - {fourth_cat_minutes_by_xpath.text}")
print(f"Page moto - {moto.text}")

driver.quit()
