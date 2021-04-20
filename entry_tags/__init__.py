import sqlite3
import json
from models import Entry_tag, Tag

def get_entry_tags_by_entry(entry_id):
    with sqlite3.connect("./journal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
            et.id,
            et.entry_id,
            et.tag_id,
            t.name
        FROM entry_tag et
        WHERE et.entry_id = ?
        JOIN tag t
            ON t.id = et.tag_id
        """, ( entry_id, ))

        entry_tags = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            entry_tag = Entry_tag
    return json.dumps(entry_tags)
