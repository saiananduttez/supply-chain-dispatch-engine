import random
import uuid
from datetime import datetime, timedelta
from database import init_db, insert_orders

CUSTOMER_NAMES = [
    "Aarav Sharma", "Priya Patel", "Vikram Malhotra", "Ananya Iyer",
    "Rohan Verma", "Sneha Kulkarni", "Karthik Nair", "Pooja Reddy",
    "David Miller", "Elena Rostova", "Marcus Vance", "Sarah Jenkins"
]

WAREHOUSE_HUBS = [
    ("WH_CENTRAL", "Midwest Central Hub", "Midwest"),
    ("WH_EAST", "New Jersey Port Terminal", "Northeast"),
    ("WH_WEST", "Pacific Coast Logistics Hub", "West Coast"),
    ("WH_SOUTH", "Gulf Logistics Hub", "Southeast"),
]

CATEGORIES = ["Consumer Electronics", "Industrial Hardware", "Home Essentials", "Automotive Parts"]

def generate_orders(num_orders=150):
    """Simulates multi-hub warehouse fulfillment orders with dispatch lead-time calculation."""
    orders = []
    base_time = datetime.now() - timedelta(days=14)

    for i in range(num_orders):
        order_id = f"ORD_{str(uuid.uuid4())[:8]}"
        cust_name = random.choice(CUSTOMER_NAMES)
        wh_code, wh_name, region = random.choice(WAREHOUSE_HUBS)
        cat = random.choice(CATEGORIES)
        units = random.randint(1, 15)

        order_dt = base_time + timedelta(hours=i * 2 + random.randint(1, 4))
        
        # Simulating operational bottlenecks: ~80% dispatched, ~12% delayed, ~8% backordered
        status = random.choices(["Dispatched", "Delayed", "Backordered"], weights=[0.80, 0.12, 0.08])[0]

        if status == "Dispatched":
            # Typical dispatch within 4 to 28 hours
            dispatch_hours = random.randint(4, 28)
            dispatch_dt = order_dt + timedelta(hours=dispatch_hours)
            lead_time = round(float(dispatch_hours), 2)
            dispatch_str = dispatch_dt.strftime("%Y-%m-%d %H:%M:%S")
        elif status == "Delayed":
            # Delayed orders take 36 to 72 hours
            dispatch_hours = random.randint(36, 72)
            dispatch_dt = order_dt + timedelta(hours=dispatch_hours)
            lead_time = round(float(dispatch_hours), 2)
            dispatch_str = dispatch_dt.strftime("%Y-%m-%d %H:%M:%S")
        else:
            # Backordered: not yet dispatched
            dispatch_str = None
            lead_time = None

        orders.append((
            order_id,
            cust_name,
            wh_name,
            region,
            cat,
            units,
            order_dt.strftime("%Y-%m-%d %H:%M:%S"),
            dispatch_str,
            status,
            lead_time
        ))

    return orders

if __name__ == "__main__":
    init_db()
    order_data = generate_orders(150)
    insert_orders(order_data)
    print(f"Success: Ingested {len(order_data)} fulfillment orders across warehouse hubs.")