"""Small script to create a demo SQLite DB with fake sample data.
This file is safe to commit and will be used by the demo to provide reproducible sample data.
"""
import sqlite3
from pathlib import Path

def create_demo_db(path: str = "agente_database/demo_sample.db"):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(p))
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS inventory_items (
        item_name TEXT PRIMARY KEY,
        quantity REAL,
        unit TEXT,
        cost_per_unit REAL
    )
    ''')
    cur.execute('''
    INSERT OR IGNORE INTO inventory_items (item_name, quantity, unit, cost_per_unit) VALUES
    ('Farina', 25.0, 'kg', 0.45),
    ('Zucchero', 10.0, 'kg', 0.60),
    ('Uova', 200.0, 'pcs', 0.10)
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,
        category TEXT,
        amount REAL,
        description TEXT,
        date TEXT
    )
    ''')
    cur.execute('''
    INSERT OR IGNORE INTO transactions (type, category, amount, description, date) VALUES
    ('revenue', 'sales', 1500.0, 'Vendite giornaliere', '2025-08-01'),
    ('expense', 'utilities', 200.0, 'Bollette', '2025-08-02')
    ''')

    conn.commit()
    conn.close()
    print(f"Created demo db at {p}")

if __name__ == '__main__':
    create_demo_db()
