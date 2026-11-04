
import pandas as pd
import random

random.seed(42)

# Original data from assignment PDF
data = [
    ["O1", "C001", "Wireless Mouse", "electronics", 3, 20.0,
     "R001", "Works fine but the battery died in a week.", "mixed", "positive", "original"],

    ["O2", "C002", "wireless mouse", "Electronics", 2, 20.0,
     "R002", "Exactly what I needed, five stars!", "positive", "positive", "original"],

    ["O3", "C003", "Yoga Mat", "", 5, 15.0,
     "R003", "Arrived broken, waste of money.", "negative", "negative", "original"],

    ["O4", "C003", "Desk Lamp", "Home", 1, 25.0,
     "R004", "It's okay, nothing special.", "neutral", "positive", "original"],

    ["O5", "C002", "Yoga Mat", "Fitness", 2, 15.0,
     None, None, None, None, "original"]
]

# Synthetic products and reviews
products = [
    ("Bluetooth Headphones", "Electronics", 45.0),
    ("Water Bottle", "Fitness", 12.0),
    ("Office Chair", "Home", 120.0),
    ("Keyboard", "Electronics", 30.0),
    ("Dumbbells", "Fitness", 35.0)
]

reviews = [
    ("Excellent product, very happy!", "positive"),
    ("Poor quality, stopped working.", "negative"),
    ("Average product, nothing special.", "neutral"),
    ("Good quality but delivery was late.", "mixed")
]

customers = ["C001", "C002", "C003", "C004", "C005"]

# Generate 20 synthetic orders with reviews
for i in range(1, 21):

    product, category, price = random.choice(products)
    review_text, sentiment = random.choice(reviews)

    data.append([
        f"SO{i:03d}",
        random.choice(customers),
        product,
        category,
        random.randint(1, 5),
        price,
        f"SR{i:03d}",
        review_text,
        sentiment,
        sentiment,
        "synthetic"
    ])

# Create one DataFrame
columns = [
    "order_id",
    "customer_id",
    "product",
    "category",
    "qty",
    "unit_price",
    "review_id",
    "review_text",
    "reference_sentiment",
    "llm_sentiment",
    "data_source"
]

df = pd.DataFrame(data, columns=columns)

# Save one CSV
df.to_csv("ecommerce_dataset.csv", index=False)

print("Dataset generated successfully!")
print("Total records:", len(df))
print(df.head())
