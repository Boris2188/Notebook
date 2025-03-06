import sqlite3

def creat_table(name_db: str):
    with sqlite3.connect(name_db) as conn:
        cur = conn.cursor()
        cur.execute("""CREAT TABLE IF NOT EXESTS contacts(
        id INTEGER PRIMARY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT DEFAULT NULL,
        telegram_name TEXT NOT NULL,
        vk_name TEXT DEFAULT NULL,
        phone_number TEXT DEFAULT NULL,
        )
        """)
