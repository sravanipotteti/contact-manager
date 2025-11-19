import sqlite3

DB_NAME = "contacts.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # access columns by name
    return conn


def get_all_contacts():
    conn = get_connection()
    contacts = conn.execute(
        "SELECT * FROM contacts ORDER BY created_at DESC"
    ).fetchall()
    conn.close()
    return contacts


def get_contact(contact_id: int):
    conn = get_connection()
    contact = conn.execute(
        "SELECT * FROM contacts WHERE id = ?",
        (contact_id,)
    ).fetchone()
    conn.close()
    return contact


def create_contact(name: str, email: str, phone: str, address: str):
    conn = get_connection()
    conn.execute(
        "INSERT INTO contacts (name, email, phone, address) VALUES (?, ?, ?, ?)",
        (name, email, phone, address)
    )
    conn.commit()
    conn.close()


def update_contact(contact_id: int, name: str, email: str, phone: str, address: str):
    conn = get_connection()
    conn.execute(
        """
        UPDATE contacts
        SET name = ?, email = ?, phone = ?, address = ?
        WHERE id = ?
        """,
        (name, email, phone, address, contact_id)
    )
    conn.commit()
    conn.close()


def delete_contact(contact_id: int):
    conn = get_connection()
    conn.execute(
        "DELETE FROM contacts WHERE id = ?",
        (contact_id,)
    )
    conn.commit()
    conn.close()

def search_contacts(query: str):
    conn = get_connection()
    like_pattern = f"%{query}%"
    contacts = conn.execute(
        """
        SELECT * FROM contacts
        WHERE
            name    LIKE ?
            OR email   LIKE ?
            OR phone   LIKE ?
            OR address LIKE ?
        ORDER BY created_at DESC
        """,
        (like_pattern, like_pattern, like_pattern, like_pattern)
    ).fetchall()
    conn.close()
    return contacts
