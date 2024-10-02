import sqlite3

# Verbindung zur Datenbank
def create_connection():
    conn = sqlite3.connect('todorpg.db')
    return conn

# Tabellen erstellen
def setup_database():
    conn = create_connection()
    cursor = conn.cursor()

    # Benutzer-Tabelle
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            race TEXT,
            class TEXT,
            image TEXT,
            level INTEGER DEFAULT 1,
            xp INTEGER DEFAULT 0
        )
    ''')

    # Quest-Tabelle
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quest (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT NOT NULL,
            status TEXT DEFAULT 'offen',
            due_date DATE,
            difficulty TEXT,
            xp_award INTEGER,
            FOREIGN KEY(user_id) REFERENCES user(id) ON DELETE CASCADE
        )
    ''')

    conn.commit()
    conn.close()

# Beispiel: Setup der Datenbank aufrufen
if __name__ == '__main__':
    setup_database()
