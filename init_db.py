import sqlite3

def init_db():
    conn = sqlite3.connect("contacts.db")
    with open("schema.sql", "r") as f:
        conn.executescript(f.read())
    conn.close()
    print("Database initialized ✅")

if __name__ == "__main__":
    init_db()
