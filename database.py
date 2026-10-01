import sqlite3

def init_db(db_name="supply_chain.db"):
    """Initializes tables for warehouse locations and fulfillment orders."""
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS fulfillment_orders (
        order_id TEXT PRIMARY KEY,
        customer_name TEXT,
        warehouse_hub TEXT,
        region TEXT,
        item_category TEXT,
        order_units INTEGER,
        order_timestamp TIMESTAMP,
        dispatch_timestamp TIMESTAMP,
        dispatch_status TEXT,
        lead_time_hours REAL
    );
    """)
    conn.commit()
    conn.close()

def insert_orders(orders, db_name="supply_chain.db"):
    """Batch inserts fulfillment records into the database."""
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.executemany("""
    INSERT OR IGNORE INTO fulfillment_orders
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, orders)
    conn.commit()
    conn.close()