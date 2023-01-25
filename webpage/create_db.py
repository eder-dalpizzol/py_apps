import sqlite3

def create_database_and_tables():
  # Connect to the database (or create it if it doesn't exist)
  conn = sqlite3.connect('database.db')

  # Create a cursor object
  cursor = conn.cursor()

  # Create the table (if it doesn't exist)
  cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)''')

  # Commit the changes
  conn.commit()

  # Close the connection
  conn.close()
