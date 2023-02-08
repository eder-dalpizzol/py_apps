import sqlite3, os

def create_db():
  print(os.path.join(os.getcwd(), 'db'))
  db_dir = os.path.join(os.getcwd(), 'db')
  if not os.path.exists(db_dir):
      os.makedirs(db_dir)

  db_path = os.path.join(db_dir, 'db.db')
  conn = sqlite3.connect(db_path)
  cursor = conn.cursor()
  
  # Create the products table if it doesn't exist
  cursor.execute('''
      CREATE TABLE IF NOT EXISTS products (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          descricao TEXT NOT NULL,
          preco REAL NOT NULL,
          qtde INTEGER NOT NULL,
          codebar TEXT NOT NULL
      );
  ''')

  cursor.execute('''
    CREATE TABLE  IF NOT EXISTS kardex (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NULL,
    mov_type TEXT NULL,
    price REAL DEFAULT 0,
    general_info TEXT NULL,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  );
    ''')


  # Commit the changes and close the connection
  conn.commit()
  cursor.close()
  conn.close()

create_db()