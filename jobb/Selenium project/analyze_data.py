import csv
import json

# Function to analyze the CSV data
def analyze_data(file_path):
    products = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row
        for row in reader:
            title, price, discount = row
            discount_percentage = extract_discount_percentage(discount)
            if discount_percentage > 50:
                products.append({'Title': title, 'Price': price, 'Discount': discount})
    return products

def extract_discount_percentage(discount):
    # Extract percentage from discount string (e.g., "Save 60%")
    if "%" in discount:
        return int(discount.strip().split("%")[0].split()[-1])
    return 0

# Function to save data to JSON
def save_to_json(products, file_path='discounted_products.json'):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(products, file, ensure_ascii=False, indent=4)
        print("Analysis completed and data saved to discounted_products.json")
    except Exception as e:
        print(f"Error saving to JSON: {e}")

# Analyze the data
file_path = 'amazon_best_sellers.csv'
discounted_products = analyze_data(file_path)

# Print the products with discounts greater than 50%
print("Products with discounts greater than 50%:")
for product in discounted_products:
    print(f"Title: {product['Title']}, Price: {product['Price']}, Discount: {product['Discount']}")

# Save the analyzed data to JSON
save_to_json(discounted_products)





