import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. Load Reviews Dataset
df = pd.read_csv("part_b_reviews.csv")

# 2. Compare Reference and LLM Sentiments
y_true = df["reference_sentiment"].str.lower()
y_pred = df["llm_sentiment"].str.lower()

# 3. Calculate Accuracy
accuracy = accuracy_score(y_true, y_pred)

print("Sentiment Accuracy:", round(accuracy * 100, 2), "%")

# 4. Classification Report
print("Classification Report:")
print(classification_report(y_true, y_pred, zero_division=0))

# 5. Identify Incorrect Predictions
df["correct"] = y_true == y_pred

print("Incorrect Predictions:")
print(df[~df["correct"]]
      [["review_id", "customer_id", "product_id", "review_text", "reference_sentiment", "llm_sentiment"]])