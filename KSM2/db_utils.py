# db_utils.py

import sqlite3

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cash_register (
            id INTEGER PRIMARY KEY,
            place TEXT,
            issues TEXT,
            accepts TEXT,
            amount TEXT,
            code TEXT,
            has_recount BOOLEAN
        )
    """)
    conn.commit()
    conn.close()

def save_cash_register(data):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO cash_register (place, issues, accepts, amount, code, has_recount)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (data["place"], data["issues"], data["accepts"], data["amount"], data["code"], data["has_recount"]))
    conn.commit()
    conn.close()
