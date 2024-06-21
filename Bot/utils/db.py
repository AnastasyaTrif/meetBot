import sqlite3

def init_db():
    conn = sqlite3.connect('db/meetings.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS meetings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            date TEXT,
            preference TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_meeting(user_id, date, preference):
    conn = sqlite3.connect('db/meetings.db')
    c = conn.cursor()
    c.execute("INSERT INTO meetings (user_id, date, preference) VALUES (?, ?, ?)",
              (user_id, date, preference))
    conn.commit()
    conn.close()

def get_meetings():
    conn = sqlite3.connect('db/meetings.db')
    c = conn.cursor()
    c.execute("SELECT date, preference FROM meetings")
    meetings = c.fetchall()
    conn.close()
    return meetings

init_db()
