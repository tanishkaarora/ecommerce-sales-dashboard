import requests
import random

url = "http://127.0.0.1:8000/sales"

products = ["Mobile", "Laptop", "Shoes", "T-Shirt", "Book"]
categories = ["Electronics", "Clothing", "Grocery", "Books"]

for i in range(50):
    data = {
        "product_name": random.choice(products),
        "category": random.choice(categories),
        "price": random.randint(500, 60000),
        "quantity": random.randint(1, 5)
    }
    requests.post(url, json=data)

print("50 sales records added successfully")
