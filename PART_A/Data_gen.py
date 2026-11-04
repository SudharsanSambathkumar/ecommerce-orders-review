
import pandas as pd
import random

random.seed(42)

# Original data from assignment PDF
data = [
    ["O1", "Wireless Mouse", "electronics", 3, 20.0],
    ["O2", "wireless mouse", "Electronics", 2, 20.0],
    ["O3", "Yoga Mat", "", 5, 15.0],
    ["O4", "Desk Lamp", "Home", 1, 25.0],
    ["O5", "Yoga Mat", "Fitness", 2, 15.0]
]
# Synthetic products
products = [
    ("Wireless Mouse", "Electronics", 20.0),
    ("Yoga Mat", "Fitness", 15.0),
    ("Desk Lamp", "Home", 25.0),
    ("Bluetooth Headphones", "Electronics", 45.0),
    ("Water Bottle", "Fitness", 12.0),
    ("Office Chair", "Home", 120.0),
    ("Keyboard", "Electronics", 30.0),
    ("Dumbbells", "Fitness", 35.0),
    ("Laptop Stand", "Home", 28.0),
    ("Resistance Bands", "Fitness", 18.0)
]



# Generate 96 synthetic orders with reviews
for i in range(6, 101):
    product, category, price = random.choice(products)

    # Random missing categories  with 20% probability
    if random.random() < 0.20:
        category = None

    data.append([
        f"O{i}",
        product,
        category,
        random.randint(1, 5),
        price
    ])

# Create one DataFrame
columns = [
    "order_id",
    "product",
    "category",
    "qty",
    "unit_price"
]

df = pd.DataFrame(data, columns=columns)

# Save one CSV
df.to_csv("ecommerce_dataset.csv", index=False)

print("Dataset generated successfully!")
print("Total records:", len(df))
print(df.head())
