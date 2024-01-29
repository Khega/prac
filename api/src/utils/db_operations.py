import mysql.connector
from api.src.utils.db import db_config

def db_update_item(query):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def db_delete_item(query):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        conn.commit()
    finally:
        cursor.close()
        conn.close()
