import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseManager:
    """Class for managing SQLite database."""
    

    def __init__(self, db_name=None):
        """
        Initialize DatabaseManager.

        Args:
            db_name (str): Name of the SQLite database.
        """
        # Ustawienie nazwy bazy danych
        if db_name is None:
             db_name = os.getenv("DB_NAME", ".zad3/passwords.db")
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        
        # Utworzenie połączenia z bazą danych
        self.conn = sqlite3.connect(self.db_name)
        self.conn = sqlite3.connect(db_name)

    def create_table(self):
        """Create passwords table if it does not exist."""
        query = '''CREATE TABLE IF NOT EXISTS passwords (
                    id INTEGER PRIMARY KEY,
                    hash TEXT,
                    salt TEXT
                )'''
        self.conn.execute(query)

    def insert_password(self, hash_value, salt):
        """
        Insert hashed password and salt into the database.

        Args:
            hash_value (str): Hashed            
            hash_value (str): Hashed password to be inserted.
            salt (str): Salt to be inserted.
        """
        self.conn.execute('INSERT INTO passwords (hash, salt) VALUES (?, ?)', (hash_value, salt))
        self.conn.commit()

    def get_passwords(self):
        """Retrieve hashed passwords and salts from the database."""
        cursor = self.conn.execute('SELECT hash, salt FROM passwords')
        return cursor.fetchall()

    def close_connection(self):
        """Close connection to the database."""
        self.conn.close()

