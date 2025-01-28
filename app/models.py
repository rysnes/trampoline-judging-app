import sqlite3

# Function to create database tables
def create_tables():
    conn = sqlite3.connect('instance/database.db')
    cursor = conn.cursor()

    # Challenges Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS challenges (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT UNIQUE NOT NULL, 
            video_url TEXT NOT NULL,
            labels TEXT NOT NULL, 
            correct_scores TEXT NOT NULL, 
            explanation TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
    print("Database tables created successfully.")
