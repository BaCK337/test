import sqlite3

def connect_db():
    conn = sqlite3.connect('users.db')
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        telegram_id INTEGER NOT NULL,
                        email TEXT,
                        status TEXT DEFAULT 'pending')''')
    conn.commit()
    conn.close()

def insert_user(telegram_id, email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (telegram_id, email) VALUES (?, ?)", (telegram_id, email))
    conn.commit()
    conn.close()

def get_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE status='pending'")
    users = cursor.fetchall()
    conn.close()
    return users

def update_user_status(user_id, status):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET status=? WHERE id=?", (status, user_id))
    conn.commit()
    conn.close()
