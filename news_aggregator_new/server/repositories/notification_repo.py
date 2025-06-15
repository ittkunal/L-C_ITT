from server.db.db import get_db_connection

def get_users_for_notification():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT u.email, n.keywords FROM users u JOIN notifications n ON u.id = n.user_id WHERE n.enabled=1")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users