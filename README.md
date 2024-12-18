# selenium_project
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import json

# Path to your ChromeDriver
CHROME_DRIVER_PATH = 'C:\\Users\\HP\\OneDrive\\Desktop\\jobb\\Selenium project\\chromedriver.exe'

# Initialize WebDriver
try:
    print("Initializing WebDriver...")
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    print("WebDriver initialized successfully!")
except Exception as e:
    print(f"Error initializing WebDriver: {e}")

# Function to log in to Amazon
def login_amazon(driver, username, password):
    try:
        driver.get('https://www.amazon.in/ap/signin')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ap_email')))
        driver.find_element(By.ID, 'ap_email').send_keys(username)
        driver.find_element(By.ID, 'continue').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ap_password')))
        driver.find_element(By.ID, 'ap_password').send_keys(password)
        driver.find_element(By.ID, 'signInSubmit').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'nav-link-accountList')))
        print("Logged in to Amazon successfully!")
    except Exception as e:
        print(f"Error logging in to Amazon: {e}")

# Replace 'your_email@example.com' and 'your_password' with your actual Amazon credentials
login_amazon(driver, 'your_email@example.com', 'your_password')

# Function to scrape product details
def scrape_best_sellers(driver, categories, top_n=1500):
    product_details = []
    for category_url in categories:
        try:
            driver.get(category_url)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'zg-item-immersion')))
            products = driver.find_elements(By.CLASS_NAME, 'zg-item-immersion')[:top_n]
            for product in products:
                try:
                    title = product.find_element(By.CLASS_NAME, 'p13n-sc-truncate').text
                    price_elements = product.find_elements(By.CLASS_NAME, 'p13n-sc-price')
                    price = price_elements[0].text if price_elements else "Price not available"
                    discount_elements = product.find_elements(By.CLASS_NAME, 'a-span-last')
                    discount = discount_elements[0].text if discount_elements else "Discount not available"
                    product_details.append((title, price, discount))
                except Exception as e:
                    print(f"Error scraping product: {e}")
                    continue
        except Exception as e:
            print(f"Error loading category page: {e}")
    return product_details

# Define the URLs of the categories to scrape
categories = [
    'https://www.amazon.in/gp/bestsellers/kitchen/ref=zg_bs_nav_kitchen_0',
    'https://www.amazon.in/gp/bestsellers/shoes/ref=zg_bs_nav_shoes_0',
    'https://www.amazon.in/gp/bestsellers/computers/ref=zg_bs_nav_computers_0',
    'https://www.amazon.in/gp/bestsellers/electronics/ref=zg_bs_nav_electronics_0',
    # Add more category URLs as needed
]

# Scrape product details from the specified categories
products = scrape_best_sellers(driver, categories)

# Print the scraped products to verify
print("Scraped products:", products)

# Save the data to a CSV file
def save_to_csv(products, file_path='amazon_best_sellers.csv'):
    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'Price', 'Discount'])
            writer.writerows(products)
        print("Data saved to amazon_best_sellers.csv")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

# Save the data to a JSON file
def save_to_json(products, file_path='amazon_best_sellers.json'):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(products, file, ensure_ascii=False, indent=4)
        print("Data saved to amazon_best_sellers.json")
    except Exception as e:
        print(f"Error saving to JSON: {e}")

# Save the scraped data to CSV and JSON
save_to_csv(products)
save_to_json(products)

# Close the browser
try:
    driver.quit()
    print("Browser closed")
except Exception as e:
    print(f"Error closing the browser: {e}")
