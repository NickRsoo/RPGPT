import sqlite3

DATABASE_NAME = "rpg_todo.db"

def create_connection():
    """Erstellt eine Verbindung zur Datenbank."""
    return sqlite3.connect(DATABASE_NAME)

def init_db():
    """Initialisiert die Datenbank und erstellt die Tabelle, falls sie nicht existiert."""
    with create_connection() as connection:
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS characters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            level INTEGER DEFAULT 1,
            gold INTEGER DEFAULT 0,
            xp INTEGER DEFAULT 0
        )
        """)

        # Tabelle für Quests
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS quests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            xp_reward INTEGER NOT NULL,
            gold_reward INTEGER NOT NULL,
            difficulty TEXT NOT NULL,
            due_date TEXT NOT NULL,
            completed BOOLEAN DEFAULT 0,
            charactername INTEGER NOT NULL
        )
        """)
        connection.commit()

    
def save_character(name, level=1, gold=0, xp=0):
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO characters (name, level, gold, xp) 
        VALUES (?, ?, ?, ?)
        """, (name, level, gold, xp))
        conn.commit()
def get_character(name):
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM characters WHERE name = ?
        """, (name,))
        return cursor.fetchone()
def save_quest(description, xp_reward, gold_reward, difficulty, due_date, character_name):
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO quests (description, xp_reward, gold_reward, difficulty, due_date, character_name)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (description, xp_reward, gold_reward, difficulty, due_date, character_name))
        conn.commit()
def get_quests(character_name):
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM quests WHERE character_id = ? AND completed = 0
        """, (character_name,))
        return cursor.fetchall()

