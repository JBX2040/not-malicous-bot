from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Path to your chromedriver executable
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'

# URL of the webpage you want to automate
URL = 'https://maxnest0x0.github.io/rysteria'

# Function to perform the repetitive tasks
def perform_tasks():
    # Launch Chrome browser
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
    
    # Open the webpage
    driver.get(URL)
    
    try:
        # Find the input field
        input_field = driver.find_element_by_tag_name('input')
        
        # Perform the repetitive tasks
        while True:
            input_field.send_keys(Keys.ENTER)
            time.sleep(0.5)  # Wait for the page to respond
            
            input_field.send_keys(Keys.ENTER)
            time.sleep(0.5)  # Wait for the page to respond
            
            input_field.send_keys('dinorr.fun')
            input_field.send_keys(Keys.ENTER)
            time.sleep(0.5)  # Wait for the page to respond
            
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser window
        driver.quit()

# Call the function to start performing the tasks
perform_tasks()
