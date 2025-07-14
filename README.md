
# 🦆 DuckDB + DuckLake Demo: Transaction Rollback Example

This repository demonstrates how to use the [DuckLake](https://github.com/duckdblabs/ducklake) extension with [DuckDB](https://duckdb.org) to manage external data lakes, simulate transactional behavior, and handle rollbacks using Python.

---

## 📦 What It Does

* Installs and loads the `ducklake` extension
* Attaches a DuckLake-backed data lake
* Creates `orders` and `inventory` tables
* Inserts initial inventory data
* Attempts a transaction that **fails** and is **rolled back**
* Shows how transactional consistency is preserved even in error scenarios

---

## 🧰 Requirements

* Python 3.8+
* [DuckDB Python](https://duckdb.org/docs/api/python/installation)
* DuckLake extension (auto-installed in the script)
* Optional: `pandas` for better dataframe display

Install dependencies:

```bash
pip install duckdb
```

---

## 📁 Project Structure

```
.
├── data/                  # (Auto-created by DuckLake if not present)
├── ducklake_demo.db       # DuckDB database file
└── demo_ducklake.py       # Main script
```

---

## ▶️ How to Run

```bash
python demo_ducklake.py
```

---

## 💡 What You'll See

The script:

1. Sets up the DuckLake-backed schema
2. Inserts an order and updates inventory
3. Tries to insert a **duplicate order ID** (violating the schema)
4. **Rolls back** all operations in the transaction
5. Prints the final state of the tables

### ✅ Sample Output

```
--- Starting transaction demo ---
Inserting into orders...
Updating inventory...
Inserting duplicate order_id (expected to fail)...
Error: Constraint Error: UNIQUE constraint failed: lake.orders.order_id
Transaction rolled back — no changes applied.

--- Final state ---
Orders:
Empty DataFrame
Inventory:
   product_id  quantity
0           1       100
1           2        50
2           3        75
```

---

## 🧠 Key Concepts

* **DuckLake** lets DuckDB interact with external storage (like S3 or local folders) via table-backed formats like Parquet or Iceberg.
* **Transactions** in DuckDB behave predictably even with `ATTACH`ed DuckLake schemas.
* **Rollback** ensures data consistency when constraints are violated or errors occur.

---

## 🗂️ Code Overview

### `setup_schema(conn)`

* Installs and loads DuckLake
* Attaches a virtual lake at `./data`
* Creates two tables: `orders` and `inventory`

### `demo_failed_transaction(conn)`

* Starts a transaction
* Performs valid inserts and updates
* Fails on inserting a duplicate `order_id`
* Rolls back the entire transaction

---

## 📚 References

* [DuckDB Docs](https://duckdb.org/docs/)
* [DuckLake GitHub](https://github.com/duckdblabs/ducklake)

---

## 📌 License

MIT License

---

