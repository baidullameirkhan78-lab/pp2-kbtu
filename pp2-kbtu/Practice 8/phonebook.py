import psycopg2
from config import DB_CONFIG

def get_conn():
    return psycopg2.connect(**DB_CONFIG)

def search(pattern):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
            for row in cur.fetchall():
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

if __name__ == "__main__":
    print("=== Upsert ===")
    upsert("Алия", "+77771234567")

    print("=== Іздеу ===")
    search("Алия")

    print("=== 1-бет ===")
    get_page(1)

    print("=== Топтық енгізу ===")
    bulk_insert(["Нур", "Тест"], ["+77001112233", "abc123"])

    print("=== Жою ===")
    delete("Алия")