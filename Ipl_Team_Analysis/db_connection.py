import mysql.connector

def get_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Ahkalya',  
            database='IPL_DATA_DB'
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Database Connection Error: {err}")
        return None
