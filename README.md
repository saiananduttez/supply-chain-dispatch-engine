# E-Commerce Dynamic Fulfillment & Warehouse Dispatch Engine

An automated supply chain data ingestion pipeline and SQL analytics engine tracking multi-hub warehouse dispatch operations, inventory turnaround velocity, and fulfillment SLA bottlenecks.

## Overview
Retail and supply chain operations require tight monitoring of fulfillment pipelines to prevent inventory stockouts, maintain shipping SLAs, and resolve cross-docking bottlenecks. This system simulates transactional dispatch logs across distributed regional hubs, records them in a normalized SQLite database, and computes dispatch latency and fulfillment efficiency metrics.

## Tech Stack
- Python 3
- pandas, sqlite3, uuid, datetime
- SQLite Relational Database

## Key Features
- Multi-Hub Order Pipeline: Ingests 150+ transactional order events across four major regional logistics centers (Midwest, Northeast, West Coast, Southeast).
- Dispatch SLA Monitoring: Segregates normal shipments, delay exceptions (36–72 hrs), and unfulfilled backorders.
- Inventory Turnaround Velocity: Tracks category-level unit movement and dispatch lead-time benchmarks (hours) across high-volume product categories.

## How to Run Locally

Clone or download the repository:
```bash
git clone [https://github.com/saiananduttez/supply-chain-dispatch-engine.git](https://github.com/saiananduttez/supply-chain-dispatch-engine.git)
cd supply-chain-dispatch-engine
