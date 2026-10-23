import pandas as pd
import sqlite3
from datetime import datetime

# 1. Data Generation (Extract)
def generate_sales_data():
    raw_data = {
        'order_id': [101, 102, 103, 104, 105],
        'customer': ['Kumar', 'Priya', 'Ravi', 'Anitha', 'Suresh'],
        'product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones'],
        'price': [55000, 500, 1500, 12000, 2000],
        'quantity': [1, 2, 1, 1, 3],
        'order_date': [str(datetime.now().date())] * 5
    }
    return pd.DataFrame(raw_data)

# 2. Data Transformation (Transform)
def transform_data(df):
    df['total_amount'] = df['price'] * df['quantity']
    df['customer'] = df['customer'].str.upper()
    return df

# 3. Load into Database & Filter (Load & Query)
def load_to_database(df):
    conn = sqlite3.connect('sales_warehouse.db')
    df.to_sql('orders', conn, if_exists='replace', index=False)
    
    print("Data ETL Pipeline executed successfully!\n")
    
    # All Data Print
    result = pd.read_sql_query("SELECT * FROM orders", conn)
    print("--- All Processed Data ---")
    print(result)
    
    # SPECIFIC DATA FILTER (Example: KUMAR data only)
    query = "SELECT * FROM orders WHERE customer = 'KUMAR'"
    kumar_data = pd.read_sql_query(query, conn)
    print("\n--- Specific Data (KUMAR Only) ---")
    print(kumar_data)
    
    conn.close()

# Main Execution Flow
if __name__ == "__main__":
    raw_df = generate_sales_data()
    transformed_df = transform_data(raw_df)
    load_to_database(transformed_df)
