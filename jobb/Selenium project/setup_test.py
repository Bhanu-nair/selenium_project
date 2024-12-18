from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Ensure this path is correct and points to the location where ChromeDriver is installed
CHROME_DRIVER_PATH = 'C:\Users\HP\OneDrive\Desktop\jobb\Selenium project'

# Initialize WebDriver
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)

# Open a webpage
driver.get('https://www.amazon.in')

# Wait for a few seconds to see the browser open
time.sleep(5)

# Close the browser
driver.quit()

