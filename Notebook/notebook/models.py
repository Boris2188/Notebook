import sqlite3

def creat_table(name_db: str):
    with sqlite3.connect(name_db) as conn:
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXIST contacts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT DEFAULT NULL,
        telegram_name TEXT NOT NULL,
        vk_name TEXT DEFAULT NULL,
        phone_number TEXT DEFAULT NULL,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories(id)
        
        )
        """)

        cur.execute("""CREATE TABLE IF NOT EXIST categories(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE 
        )
        """)
