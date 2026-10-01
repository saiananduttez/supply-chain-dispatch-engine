import sqlite3
import pandas as pd

def run_supply_chain_analytics(db_name="supply_chain.db"):
    conn = sqlite3.connect(db_name)

    # 1. Warehouse Hub Operational Efficiency & Mean Lead Time (Hours)
    hub_query = """
    SELECT 
        warehouse_hub,
        region,
        COUNT(order_id) AS total_orders,
        SUM(CASE WHEN dispatch_status = 'Dispatched' THEN 1 ELSE 0 END) AS on_time_dispatches,
        SUM(CASE WHEN dispatch_status = 'Delayed' THEN 1 ELSE 0 END) AS delayed_dispatches,
        SUM(CASE WHEN dispatch_status = 'Backordered' THEN 1 ELSE 0 END) AS backordered_dispatches,
        ROUND(AVG(lead_time_hours), 2) AS avg_dispatch_lead_hours
    FROM fulfillment_orders
    GROUP BY warehouse_hub, region
    ORDER BY avg_dispatch_lead_hours ASC;
    """

    # 2. Product Category Demand & Volume Velocity
    category_query = """
    SELECT 
        item_category,
        COUNT(order_id) AS total_orders,
        SUM(order_units) AS total_units_shipped,
        ROUND(AVG(lead_time_hours), 2) AS category_avg_lead_hours
    FROM fulfillment_orders
    WHERE dispatch_status IN ('Dispatched', 'Delayed')
    GROUP BY item_category
    ORDER BY total_units_shipped DESC;
    """

    # 3. Fulfillment SLA Health Summary
    sla_query = """
    SELECT 
        dispatch_status,
        COUNT(*) AS order_count,
        ROUND((COUNT(*) * 100.0 / (SELECT COUNT(*) FROM fulfillment_orders)), 2) AS sla_percentage
    FROM fulfillment_orders
    GROUP BY dispatch_status
    ORDER BY order_count DESC;
    """

    df_hub = pd.read_sql_query(hub_query, conn)
    df_cat = pd.read_sql_query(category_query, conn)
    df_sla = pd.read_sql_query(sla_query, conn)
    conn.close()

    print("\n========================================================")
    print("      WAREHOUSE REGIONAL DISPATCH & LEAD TIME           ")
    print("========================================================")
    print(df_hub.to_string(index=False))

    print("\n========================================================")
    print("        INVENTORY CATEGORY VOLUME & VELOCITY            ")
    print("========================================================")
    print(df_cat.to_string(index=False))

    print("\n========================================================")
    print("           NETWORK FULFILLMENT SLA BREAKDOWN            ")
    print("========================================================")
    print(df_sla.to_string(index=False))

if __name__ == "__main__":
    run_supply_chain_analytics()