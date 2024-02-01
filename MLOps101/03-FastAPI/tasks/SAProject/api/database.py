import sqlite3

# Database Connection and Administration

def tables_creation(cursor, conn):
    """Create a  database if not exist. Create users and history tables.
    """
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_user INTEGER NOT NULL,
            input_text TEXT NOT NULL,
            prediction TEXT NOT NULL,
            score REAL NOT NULL
        )
    """
    )
    conn.commit()
    conn.close()
    
def db_connection():
    """Connection to the database"""
    conn = sqlite3.connect("database.db", check_same_thread=False)
    cursor = conn.cursor()
    return conn, cursor

def database_initialization():
    """Start the database and tables to api usage.
    """
    
    # create users and history table
    conn, cursor = db_connection()
    tables_creation(cursor, conn)