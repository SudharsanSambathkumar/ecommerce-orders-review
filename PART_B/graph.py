from neo4j import GraphDatabase
from dotenv import load_dotenv
import certifi
import os
import pandas as pd
load_dotenv()
os.environ.setdefault("SSL_CERT_FILE", certifi.where())
URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

driver.verify_connectivity()

print("Connected successfully!")


# 1. Load datasets
orders = pd.read_csv("part_b_orders.csv")
reviews = pd.read_csv("part_b_reviews.csv")

# Handle missing values
orders = orders.astype(object).where(pd.notna(orders), None)
reviews = reviews.astype(object).where(pd.notna(reviews), None)

# 2. Create constraints
constraints = [
    """
    CREATE CONSTRAINT customer_id IF NOT EXISTS
    FOR (c:Customer)
    REQUIRE c.customer_id IS UNIQUE
    """,
    """
    CREATE CONSTRAINT product_id IF NOT EXISTS
    FOR (p:Product)
    REQUIRE p.product_id IS UNIQUE
    """,
    """
    CREATE CONSTRAINT review_id IF NOT EXISTS
    FOR (r:Review)
    REQUIRE r.review_id IS UNIQUE
    """,
    """
    CREATE CONSTRAINT category_name IF NOT EXISTS
    FOR (c:Category)
    REQUIRE c.category_name IS UNIQUE
    """
]

# 3. Product and Category
product_query = """
UNWIND $rows AS row
WITH row
WHERE row.product_id IS NOT NULL

MERGE (p:Product {product_id: row.product_id})
SET p.product_name = row.product

WITH p, coalesce(row.category, 'Uncategorized') AS category
MERGE (cat:Category {category_name: category})
MERGE (p)-[:BELONGS_TO]->(cat)
"""

# 4. Customer and Purchase
purchase_query = """
UNWIND $rows AS row
WITH row
WHERE row.customer_id IS NOT NULL
AND row.product_id IS NOT NULL

MERGE (c:Customer {customer_id: row.customer_id})
MERGE (p:Product {product_id: row.product_id})

MERGE (c)-[r:PURCHASED {order_id: row.order_id}]->(p)
SET r.quantity = row.qty,
    r.unit_price = row.unit_price
"""

# 5. Customer and Review
review_query = """
UNWIND $rows AS row
WITH row
WHERE row.customer_id IS NOT NULL
AND row.product_id IS NOT NULL

MERGE (c:Customer {customer_id: row.customer_id})
MERGE (p:Product {product_id: row.product_id})

MERGE (r:Review {review_id: row.review_id})
SET r.review_text = row.review_text,
    r.reference_sentiment = row.reference_sentiment,
    r.llm_sentiment = row.llm_sentiment

MERGE (c)-[:WROTE]->(r)
MERGE (r)-[:REVIEWS]->(p)
"""

# 6. Import into Neo4j AuraDB
try:
    with driver.session() as session:

        for query in constraints:
            session.run(query).consume()

        session.run(
            product_query,
            rows=orders.to_dict("records")
        ).consume()

        session.run(
            purchase_query,
            rows=orders.to_dict("records")
        ).consume()

        session.run(
            review_query,
            rows=reviews.to_dict("records")
        ).consume()

    print("Orders imported successfully!")
    print("Reviews imported successfully!")
    print("Graph database populated!")

finally:
    driver.close()