# Real-Time E-Commerce Data Pipeline (ETL)

## 📌 Project Overview
This project demonstrates an end-to-end **ETL (Extract, Transform, Load)** pipeline built using Python and SQLite. It simulates real-time e-commerce order transactions, applies business transformation logic, and loads structured data into a Data Warehouse table.

---

## 🛠️ Architecture & Tech Stack
* **Language:** Python 3.x
* **Data Processing:** Pandas
* **Database:** SQLite (Relational Data Warehouse)
* **Version Control:** Git & GitHub

---

## ⚙️ Data Pipeline Logic

1. **Extract:** Generates synthetic e-commerce sales transaction data (Order ID, Customer, Product, Price, Quantity, Date).
2. **Transform:** 
   * Calculates `total_amount` for each order (`price * quantity`).
   * Normalizes customer names to uppercase for data consistency.
3. **Load:** Writes the processed DataFrame into a relational table (`orders`) inside `sales_warehouse.db`.

---

## 🚀 How to Run the Project

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Kalairaksha/data-engineering-lab1.git](https://github.com/Kalairaksha/data-engineering-lab1.git)
   cd data-engineering-lab1
