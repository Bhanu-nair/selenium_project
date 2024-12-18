from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Path to your ChromeDriver
CHROME_DRIVER_PATH = 'C:\\Users\\HP\\OneDrive\\Desktop\\jobb\\Selenium project\\chromedriver.exe'

print("Initializing WebDriver...")
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)
print("WebDriver initialized successfully!")

# Open a webpage
driver.get('https://www.amazon.in')
print("Navigated to Amazon.in")

# Wait for a few seconds to see the browser open
time.sleep(5)

# Close the browser
driver.quit()
print("Browser closed")

