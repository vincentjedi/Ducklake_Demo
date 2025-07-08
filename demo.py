import duckdb

def setup_schema(conn):
    conn.execute("INSTALL 'ducklake'")
    conn.execute("LOAD 'ducklake'")
    conn.execute("ATTACH 'ducklake:demo.ducklake' AS lake (DATA_PATH './data')")

    # Drop tables if rerunning
    conn.execute("DROP TABLE IF EXISTS lake.orders")
    conn.execute("DROP TABLE IF EXISTS lake.inventory")

    # Create tables
    conn.execute("""
        CREATE TABLE lake.orders (
            order_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            customer_name TEXT
        )
    """)

    conn.execute("""
        CREATE TABLE lake.inventory (
            product_id INTEGER,
            quantity INTEGER
        )
    """)

    # Insert initial inventory
    conn.execute("INSERT INTO lake.inventory VALUES (1, 100), (2, 50), (3, 75)")

def demo_failed_transaction(conn):
    """Demonstrate a failed transaction with rollback."""
    print("\n--- Starting transaction demo ---")
    try:
        conn.execute("BEGIN TRANSACTION")

        print("Inserting into orders...")
        conn.execute("""
            INSERT INTO lake.orders (order_id, product_id, quantity, customer_name)
            VALUES (2, 2, 10, 'Bob')
        """)

        print("Updating inventory...")
        conn.execute("""
            UPDATE lake.inventory 
            SET quantity = quantity - 10 
            WHERE product_id = 2
        """)

        print("Inserting duplicate order_id (expected to fail)...")
        conn.execute("""
            INSERT INTO lake.orders (order_id, product_id, quantity, customer_name)
            VALUES (1, 3, 5, 'Bob')  -- Duplicate!
        """)

        conn.execute("COMMIT")
        print("COMMIT succeeded (this should not happen)")

    except Exception as e:
        print(f"Error: {e}")
        conn.execute("ROLLBACK")
        print("Transaction rolled back — no changes applied.")

    print("\n--- Final state ---")
    print("Orders:")
    print(conn.execute("SELECT * FROM lake.orders").fetchdf())

    print("Inventory:")
    print(conn.execute("SELECT * FROM lake.inventory").fetchdf())

if __name__ == "__main__":
    conn = duckdb.connect("ducklake_demo.db")
    setup_schema(conn)
    demo_failed_transaction(conn)
