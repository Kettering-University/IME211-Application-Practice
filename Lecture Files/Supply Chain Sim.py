# Simplified Supply Chain Simulation

# 1. Dictionary of products with their prices
products = {
    "Laptop": 1200,
    "Smartphone": 800,
    "Tablet": 450,
    "Headphones": 150,
    "Charger": 25
}

# 2. List of suppliers and their product offerings (use tuples for suppliers)
suppliers = [
    ("Supplier A", ["Laptop", "Smartphone", "Headphones"]),
    ("Supplier B", ["Tablet", "Charger"]),
    ("Supplier C", ["Laptop", "Charger"])
]

# 3. Dictionary to store orders and their statuses (e.g., 'Pending', 'Shipped', 'Delivered')
orders = {
    1001: {"status": "Pending", "items": {"Laptop": 2, "Charger": 5}},
    1002: {"status": "Shipped", "items": {"Smartphone": 1, "Headphones": 2}},
    1003: {"status": "Delivered", "items": {"Tablet": 3, "Charger": 1}}
}

# TODO: Activity - Calculate the total cost of an order using a for loop

