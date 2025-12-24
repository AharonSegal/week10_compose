from typing import List
from data.db_use import get_connection


class Contact:
    def __init__(self, id: int, first_name: str, last_name: str, phone_number: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
        }


def create_contact(first_name: str, last_name: str, phone_number: str) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO contacts (first_name, last_name, phone_number) "
            "VALUES (%s, %s, %s)",
            (first_name, last_name, phone_number),
        )
        conn.commit()
        return cursor.lastrowid
    finally:
        cursor.close()
        conn.close()


def get_all_contacts() -> List[Contact]:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT id, first_name, last_name, phone_number FROM contacts")
        rows = cursor.fetchall()
        # rows is a list of dicts like {"id": 1, "first_name": "...", ...}
        return [
            Contact(
                id=row["id"],
                first_name=row["first_name"],
                last_name=row["last_name"],
                phone_number=row["phone_number"],
            )
            for row in rows
        ]
    finally:
        cursor.close()
        conn.close()


def update_contact(contact_id: int, first_name: str, last_name: str, phone_number: str) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE contacts SET first_name=%s, last_name=%s, phone_number=%s "
            "WHERE id=%s",
            (first_name, last_name, phone_number, contact_id),
        )
        conn.commit()
        return cursor.rowcount > 0
    finally:
        cursor.close()
        conn.close()


def delete_contact(contact_id: int) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM contacts WHERE id=%s", (contact_id,))
        conn.commit()
        return cursor.rowcount > 0
    finally:
        cursor.close()
        conn.close()