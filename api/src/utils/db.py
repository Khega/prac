import mysql.connector

db_config = {
    "host": "your_host",
    "user": "your_username",
    "password": "your_password",
    "database": "your_database",
}

def db_create_user(query):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def db_check_username_exists(username):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    try:
        cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
        user = cursor.fetchone()
        return bool(user)
    finally:
        cursor.close()
        conn.close()


def db_reset_password():
    return None


def db_delete_item():
    return None

def db_get_data():
    return None

def db_update_item():
    return None