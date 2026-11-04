import pandas as pd
import random

random.seed(42)

# 1. load Part_A Dataset
df = pd.read_csv("C:\\Users\\Sudharsan\\Documents\\Task\\PART_A\\ecommerce_dataset.csv")

# 2. Add Customer ID
customer_mapping = {
    "O1": "C001",
    "O2": "C002",
    "O3": "C003",
    "O4": "C003",
    "O5": "C002"
}
customers = ["C001", "C002", "C003", "C004", "C005"]

df["customer_id"] = df["order_id"].map(customer_mapping)

# 3. Randomly assign customer IDs to the remaining orders
for i in range(6, 101):
    if random.random() < 0.8:  # 80% chance to assign a customer ID
        df.loc[df["order_id"] == f"O{i}", "customer_id"] = random.choice(customers)

# 4. Add Data Source
data_sources = ["source_A", "source_B", "source_C"]
df["data_source"] = random.choices(data_sources, k=len(df))


# 5. Add Product ID
product_mapping = {
    product: f"P{i:03d}"
    for i, product in enumerate(
        df["product"].dropna().str.strip().str.title().unique(),
        start=1
    )
}

df["product_id"] = (
    df["product"].str.strip().str.title().map(product_mapping)
)

# 6. Save Part B Orders Dataset
df.to_csv("part_b_orders.csv", index=False)
