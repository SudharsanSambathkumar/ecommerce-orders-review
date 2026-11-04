# E-Commerce Orders and Reviews Analysis

## Project Overview

This project focuses on analyzing e-commerce orders and customer reviews. It includes data cleaning, sales analysis, sentiment evaluation, and graph database implementation using Neo4j.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Neo4j AuraDB
- Cypher Query Language

## Project Structure

```text
PROJECT/
│
├── PART_A/
│   ├── ecommerce_dataset.csv
│   └── part_a.py
│
├── PART_B/
│   ├── part_b_orders.csv
│   ├── part_b_reviews.csv
│   ├── sentiment_evaluation.py
│   └── graph.py
│
└── README.md
```

## Part A – Data Analysis

- Loaded and cleaned the e-commerce orders dataset.
- Handled missing values and duplicate records.
- Calculated total revenue for each product category.
- Identified the top two best-selling products based on quantity.

## Part B – Sentiment Analysis and Graph Database

### Sentiment Analysis

- Compared the reference sentiment with the LLM predictions.
- Calculated sentiment accuracy.
- Identified incorrect predictions and analyzed borderline reviews.

**Accuracy: 50%**

### Neo4j Graph Database

- Created a cloud database using Neo4j AuraDB.
- Imported customer, product, category, and review data.
- Created relationships between customers, products, categories, and reviews.
- Used Cypher queries to identify products purchased by customers who submitted negative reviews.

**Final Result:** Customer C003 submitted a negative review. The query identified six products purchased by this customer.

## Installation

Install the required Python packages:

```bash
pip install pandas scikit-learn neo4j python-dotenv certifi
```

Create a `.env` file inside the Part B folder:

```env
NEO4J_URI=your_neo4j_connection_uri
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password
```

## Execution

Run the sentiment evaluation:

```bash
python sentiment_evaluation.py
```

Run the Neo4j data import:

```bash
python graph.py
```

The graph data can be viewed and queried through the Neo4j AuraDB Query interface.

## Assumptions

- Customer IDs were assigned as sample data because the original orders did not contain customer information.
- Customer and product associations for reviews were created for the graph database demonstration.
- Additional synthetic orders were used along with the original sample orders.
- The original four reviews were retained for sentiment evaluation.

## Conclusion

This project helped explore data cleaning, sales analysis, sentiment evaluation, and graph database concepts using Python and Neo4j. It also demonstrates how customer purchase history can be connected with review sentiment to identify purchasing patterns.