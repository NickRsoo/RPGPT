import sqlite3

# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect('rpgpt.db')

# Beispiel: Tabelle erstellen
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        race TEXT,
        class TEXT,
        level INTEGER DEFAULT 1,
        xp INTEGER DEFAULT 0
    )
''')

conn.commit()
conn.close()

