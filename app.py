import pandas as pd
import sqlite3
from datetime import datetime

# 1. Extract (Synthetic E-Commerce Data)
def generate_sales_data():
    raw_data = {
        'order_id': [101, 102, 103, 104, 105, 106],
        'customer': ['Kumar', 'Priya', 'Kumar', 'Anitha', 'Suresh', 'Priya'],
        'product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones', 'Mouse'],
        'price': [55000, 500, 1500, 12000, 2000, 500],
        'quantity': [1, 2, 1, 1, 3, 4],
        'order_date': [str(datetime.now().date())] * 6
    }
    return pd.DataFrame(raw_data)

# 2. Transform (Calculation & Aggregation Logic)
def transform_data(df):
    # Total revenue per order
    df['total_amount'] = df['price'] * df['quantity']
    df['customer'] = df['customer'].str.upper()
    
    # AGGREGATION: Customer-wise Total Spend Calculate Panrom
    customer_spend = df.groupby('customer')['total_amount'].sum().reset_index()
    customer_spend.rename(columns={'total_amount': 'total_spent'}, inplace=True)
    
    return df, customer_spend

# 3. Load & Query (Save Data Warehouse Tables)
def load_to_database(df, spend_df):
    conn = sqlite3.connect('sales_warehouse.db')
    
    # Table 1: Raw Fact Table
    df.to_sql('orders', conn, if_exists='replace', index=False)
    # Table 2: Aggregated Summary Table
    spend_df.to_sql('customer_summary', conn, if_exists='replace', index=False)
    
    print("ETL Pipeline with Aggregation Executed Successfully!\n")
    
    # Query Summary Data
    summary_result = pd.read_sql_query("SELECT * FROM customer_summary ORDER BY total_spent DESC", conn)
    print("--- Customer Spending Summary ---")
    print(summary_result)
    
    conn.close()

# Main Execution Flow
if __name__ == "__main__":
    raw_df = generate_sales_data()
    transformed_df, spend_summary = transform_data(raw_df)
    load_to_database(transformed_df, spend_summary)
