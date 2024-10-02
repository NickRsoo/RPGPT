# XP- und Leveling-System
def level_up_user_if_needed(conn, user_id):
    cursor = conn.cursor()
    cursor.execute('SELECT xp, level FROM user WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    
    if user:
        xp, level = user
        xp_needed = 100 * level  # Beispiel: 100 XP pro Level
    
        if xp >= xp_needed:
            # User levelt auf
            cursor.execute('UPDATE user SET level = level + 1, xp = xp - ? WHERE id = ?', (xp_needed, user_id))
            conn.commit()
            print(f"User {user_id} ist auf Level {level + 1} aufgestiegen!")
