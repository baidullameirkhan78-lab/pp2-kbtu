"""
TSIS 1 — Extended PhoneBook
Builds on Practice 7 (CRUD, CSV) and Practice 8 (procedures, pagination).
New features: groups, multiple phones, email, birthday,
JSON import/export, advanced search/filter/sort.
"""

import csv
import json
from datetime import datetime
from connect import get_connection

# ================================================================
# HELPERS
# ================================================================

def _row_to_dict(row, cursor):
    """Turn a cursor row into a dict using column names."""
    cols = [d[0] for d in cursor.description]
    return dict(zip(cols, row))

def _get_all_phones(conn, contact_id):
    """Return list of {phone, type} for a contact."""
    cur = conn.cursor()
    cur.execute("SELECT phone, type FROM phones WHERE contact_id = %s", (contact_id,))
    rows = cur.fetchall()
    cur.close()
    return [{"phone": r[0], "type": r[1]} for r in rows]

def _ensure_group(conn, group_name):
    """Return group id, inserting if needed."""
    cur = conn.cursor()
    cur.execute("SELECT id FROM groups WHERE name = %s", (group_name,))
    row = cur.fetchone()
    if row:
        cur.close()
        return row[0]
    cur.execute("INSERT INTO groups (name) VALUES (%s) RETURNING id", (group_name,))
    gid = cur.fetchone()[0]
    conn.commit()
    cur.close()
    return gid

def _print_contact(c):
    """Pretty-print a contact dict."""
    phones = c.get("phones", [])
    phone_str = ", ".join(f"{p['phone']} ({p['type']})" for p in phones) if phones else "—"
    print(f"  ID        : {c.get('id', '?')}")
    print(f"  Name      : {c.get('first_name', '')}")
    print(f"  Email     : {c.get('email') or '—'}")
    print(f"  Birthday  : {c.get('birthday') or '—'}")
    print(f"  Group     : {c.get('group_name') or '—'}")
    print(f"  Phones    : {phone_str}")
    print()

# ================================================================
# 3.1 — ADD / UPDATE CONTACT (console)
# ================================================================

def insert_from_console():
    name     = input("  Имя          : ").strip()
    email    = input("  Email        : ").strip() or None
    birthday = input("  Дата рожд. (YYYY-MM-DD, Enter — пропустить): ").strip() or None
    group    = input("  Группа (Family/Work/Friend/Other): ").strip() or "Other"

    conn = get_connection()
    try:
        gid = _ensure_group(conn, group)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO contacts (first_name, email, birthday, group_id) VALUES (%s, %s, %s, %s) RETURNING id",
            (name, email, birthday, gid)
        )
        cid = cur.fetchone()[0]
        
        # Add phones
        while True:
            phone = input("  Телефон (Enter — завершить): ").strip()
            if not phone: break
            ptype = input("  Тип (home/work/mobile): ").strip()
            if ptype not in ("home", "work", "mobile"): ptype = "mobile"
            cur.execute("INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)", (cid, phone, ptype))
        
        conn.commit()
        print("✅ Контакт добавлен!")
    finally:
        conn.close()

# ================================================================
# 3.2 — FILTER BY GROUP
# ================================================================

def filter_by_group():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM groups ORDER BY name")
    groups = cur.fetchall()
    print("  Доступные группы:")
    for g in groups:
        print(f"    [{g[0]}] {g[1]}")
    gid = input("  Введите ID группы: ").strip()

    cur.execute("""
        SELECT c.id, c.first_name, c.email, c.birthday, g.name AS group_name
        FROM contacts c LEFT JOIN groups g ON g.id = c.group_id
        WHERE c.group_id = %s ORDER BY c.first_name
    """, (gid,))
    rows = cur.fetchall()
    if not rows:
        print("  Контакты не найдены.")
        return
    for r in rows:
        contact = {"id": r[0], "first_name": r[1], "email": r[2], "birthday": r[3], "group_name": r[4]}
        conn2 = get_connection()
        contact["phones"] = _get_all_phones(conn2, r[0])
        conn2.close()
        _print_contact(contact)
    conn.close()

# ================================================================
# 3.3 — IMPORT / EXPORT / OTHERS
# ================================================================

def export_to_json():
    filename = "contacts.json"
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT c.id, c.first_name, c.email, c.birthday::TEXT, g.name FROM contacts c LEFT JOIN groups g ON g.id = c.group_id")
    result = []
    for r in cur.fetchall():
        result.append({"id": r[0], "first_name": r[1], "email": r[2], "birthday": r[3], "group": r[4], "phones": _get_all_phones(conn, r[0])})
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"✅ Экспортировано в {filename}")
    conn.close()

def menu():
    while True:
        print("\n--- PhoneBook TSIS 1 ---")
        print("1. Добавить контакт | 2. Фильтр по группе | 3. Экспорт JSON | 0. Выход")
        choice = input("Выбор: ")
        if choice == "1": insert_from_console()
        elif choice == "2": filter_by_group()
        elif choice == "3": export_to_json()
        elif choice == "0": break

if __name__ == "__main__":
    menu()