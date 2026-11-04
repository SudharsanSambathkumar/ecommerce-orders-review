import pandas as pd

# 1. Load Dataset
df = pd.read_csv("ecommerce_dataset.csv")
print("Original Shape:", df.shape)

# 2. Data Cleaning
# Remove duplicates
df = df.drop_duplicates(subset=["order_id"])

## missing Values in Data
print("Missing Values:")
print(df.isnull().sum())

## missing Product Names
df["product"] = df["product"].fillna("Unknown Product")

##missing Categories
Org_cat_mapping = df["category"].mode()

if not Org_cat_mapping.empty:
    df["category"] = df["category"].fillna(Org_cat_mapping.iloc[0])
else:
    df["category"] = df["category"].fillna("Uncategorized")

## Standardize Text Columns
text_columns = ["product", "category"]
for col in text_columns:
    df[col] = df[col].str.strip().str.title()

print("Data after cleaning:")
print(df.isnull().sum())

#3. Revenue Calculation
df["revenue"] = df["qty"] * df["unit_price"]

#4. Total Revenue by Category
total_revenue_by_category = df.groupby("category")["revenue"].sum()
print("Total Revenue by Category:")
print(total_revenue_by_category)

#5.top 2 best-selling products by quantity
top_products_by_qty = df.groupby("product")["qty"].sum().nlargest(2)
print("Top 2 Best-Selling Products by Quantity:")
print(top_products_by_qty)

#6. Save results to json
total_revenue_by_category.to_json("total_revenue_by_category.json")
top_products_by_qty.to_json("top_products_by_qty.json", orient="index")