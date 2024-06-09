from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.headless = True  # Run in headless mode

driver = webdriver.Chrome(options=options)

driver.get('https://maxnest0x0.github.io/rysteria')

try:
    # Locate the input field (update the selector to match your target)
    input_field = driver.find_element_by_tag_name('body')

    while True:

        input_field.send_keys(Keys.ENTER)
        time.sleep(1) 

        input_field.send_keys(Keys.ENTER)
        time.sleep(1) 

        input_field.send_keys("mn = bozo")
        time.sleep(1)  

        input_field.send_keys(Keys.ENTER)
        time.sleep(1)  

except Exception as e:
    print(f"An error occurred: {e}")

finally:

    driver.quit()
