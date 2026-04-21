import psycopg2
import sys
from config import DB_CONFIG

def get_conn():
    return psycopg2.connect(**DB_CONFIG)

def search(pattern):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
            for row in cur.fetchall():
                print(row)

def show_all():
    with get_conn() as conn:
        with conn.cursor() as cur:
            # Барлық деректі ID бойынша реттеп алу
            cur.execute("SELECT * FROM phonebook ORDER BY id")
            rows = cur.fetchall()
            if not rows:
                print("Кітапша бос.")
            else:
                for row in rows:
                    print(row)

def get_page(page=1, per_page=5):
    offset = (page - 1) * per_page
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM get_contacts_paginated(%s,%s)",
                (per_page, offset))
            for row in cur.fetchall():
                print(row)

def upsert(name, phone):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL upsert_contact(%s,%s)", (name, phone))
        conn.commit()

def delete(value):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL delete_contact(%s)", (value,))
        conn.commit()

def bulk_insert(names, phones):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL bulk_insert_contacts(%s,%s)", (names, phones))
        conn.commit()

import sys # Файлдың ең басына қосуды ұмытпаңыз

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Қолдану: python3 phonebook.py [add/del/search]")
        sys.exit()

    cmd = sys.argv[1]

    if cmd == "add":
        name = input("Есімі: ")
        phone = input("Нөмірі: ")
        upsert(name, phone)
        print(f"Дайын! {name} қосылды.")

    elif cmd == "all":
        show_all()


    elif cmd == "del":
        name = input("Кімді өшіреміз?: ")
        delete(name)
        print(f"Дайын! {name} өшірілді.")

    elif cmd == "search":
        name = input("Кімді іздейміз?: ")
        search(name)
