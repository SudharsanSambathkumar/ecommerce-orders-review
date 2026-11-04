import pandas as pd

# 1.Create Reviews Dataset
reviews = [
    {
        "review_id": "R001",
        "customer_id": "C001",
        "product_id": "P001",
        "review_text": "Works fine but the battery died in a week.",
        "reference_sentiment": "mixed",
        "llm_sentiment": "positive"
    },
    {
        "review_id": "R002",
        "customer_id": "C002",
        "product_id": "P002",
        "review_text": "Exactly what I needed, five stars!",
        "reference_sentiment": "positive",
        "llm_sentiment": "positive"
    },
    {
        "review_id": "R003",
        "customer_id": "C003",
        "product_id": "P003",
        "review_text": "Arrived broken, waste of money.",
        "reference_sentiment": "negative",
        "llm_sentiment": "negative"
    },
    {
        "review_id": "R004",
        "customer_id": "C001",
        "product_id": "P002",
        "review_text": "It's okay, nothing special.",
        "reference_sentiment": "neutral",
        "llm_sentiment": "positive"
    }
]

# 2. Convert to DataFrame
reviews_df = pd.DataFrame(reviews)

# 3. Save Dataset
reviews_df.to_csv("part_b_reviews.csv", index=False)

print("Reviews Dataset Created Successfully!")
print(reviews_df)