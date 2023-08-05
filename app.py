import time
import win32api
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Configure Chrome options to run in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")

# Set the Chrome driver path using webdriver_manager
chrome_driver_path = ChromeDriverManager().install()

# Start the Chrome browser
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")

# Get the initial count of unread messages
unread_count = len(driver.find_elements(By.XPATH, "//span[@class='OUeyt']"))

# Monitor for new messages
while True:
    # Get the current count of unread messages
    current_count = len(driver.find_elements(By.XPATH, "//span[@class='OUeyt']"))
    print(current_count)
    if current_count > unread_count:
        # New message received
        unread_count = current_count

        print(current_count)

    time.sleep(1)
