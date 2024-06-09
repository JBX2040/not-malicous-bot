import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def start_driver():
    options = Options()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-software-rasterizer')
    options.add_argument('--disable-web-security')
    options.add_argument('--disable-translate')
    options.add_argument('--disable-remote-fonts')
    options.add_argument('--disable-sync')
    options.add_argument('--disable-background-networking')
    options.add_argument('--disable-default-apps')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-desktop-notifications')
    options.add_argument('--disable-background-timer-throttling')
    options.add_argument('--disable-backgrounding-occluded-windows')
    options.add_argument('--disable-renderer-backgrounding')
    options.add_argument('--disable-preconnect')
    return webdriver.Chrome(options=options)

def run_bot():
    driver = start_driver()
    url = 'https://maxnest0x0.github.io/rysteria'
    logging.info(f"Opening URL: {url}")
    driver.get(url)
    try:
        input_field = driver.find_element_by_tag_name('body')
        while True:
            input_field.send_keys(Keys.ENTER)
            logging.info("Pressed Enter")
            time.sleep(1)
            input_field.send_keys(Keys.ENTER)
            logging.info("Pressed Enter again")
            time.sleep(1)
            input_field.send_keys("text")
            logging.info('Typed "text"')
            time.sleep(1)
            input_field.send_keys(Keys.ENTER)
            logging.info("Pressed Enter after typing text")
            time.sleep(1)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        driver.quit()

if __name__ == "__main__":
    while True:
        try:
            run_bot()
        except Exception as e:
            logging.error(f"Bot crashed with error: {e}")
        logging.info("Restarting bot in 5 seconds...")
        time.sleep(5)
