import sqlite3
import json
from models import Entry, Mood
from entry_tags import get_entry_tags_by_entry

def get_all_entries():
    with sqlite3.connect("./journal.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.concept,
            e.entry,
            e.mood_id, 
            m.label
        FROM entry e
        JOIN mood m
            ON m.id = e.mood_id
        """)

        entries = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['id'], row['date'], row['concept'],
                            row['entry'], row['mood_id'])

            mood = Mood(row['mood_id'], row['label'])
            entry.mood = mood.__dict__
            entry.tags = get_entry_tags_by_entry(row['id'])

            entries.append(entry.__dict__)

    return json.dumps(entries)

def get_single_entry(id):
    with sqlite3.connect("./journal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.concept,
            e.entry,
            e.mood_id
        FROM entry e
        WHERE e.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        entry = Entry(data['id'], data['date'], data['concept'],
                            data['entry'], data['mood_id'])

        return json.dumps(entry.__dict__)

def get_entries_by_search(search_term):
    with sqlite3.connect("./journal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.concept,
            e.entry,
            e.mood_id
        FROM entry e
        WHERE e.entry LIKE ?
        """, ( f'%{search_term}%', ))

        entries = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['id'], row['date'], row['concept'],
                            row['entry'], row['mood_id'])

            entries.append(entry.__dict__)

    return json.dumps(entries)

def create_entry(new_entry):
    with sqlite3.connect("./journal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Entry
            (date, concept, entry, mood_id)
        VALUES
            (?, ?, ?, ?);
        """, (new_entry['date'], new_entry['concept'],
            new_entry['entry'], new_entry['mood_id']))

        id = db_cursor.lastrowid

        new_entry['id'] = id

        for tag in new_entry['tag']:
            db_cursor.execute("""
            INSERT INTO Entry_tag
                (entry_id, tag_id)
            VALUES
                (?, ?)
            """, ( id, tag ))

    return json.dumps(new_entry)

def update_entry(id, entry):
    with sqlite3.connect("./journal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Entry
            SET
                date = ?,
                concept = ?,
                entry = ?,
                mood_id = ?
        WHERE id = ?
            """, (entry['date'], entry['concept'],
                entry['entry'], entry['mood_id'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True

def delete_entry(id):
    with sqlite3.connect("./journal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM entry
        WHERE id = ?
        """, ( id, ))