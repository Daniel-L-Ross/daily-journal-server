import sqlite3
import json
from models import Tag

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
        JOIN tag t
            ON t.id = et.tag_id
        WHERE et.entry_id = ?
        """, ( entry_id, ))

        tags = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            tag = Tag(row['tag_id'], row['name'])
            tags.append(tag.__dict__)

    return tags
