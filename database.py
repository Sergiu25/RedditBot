import sqlite3
DB_PATH=r"D:\proiecte\RedditProject\redditbotdb.db"
#initial setupd for database
def setup_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS replied_comments(
            comment_id TEXT PRIMARY KEY
        )
    """)
    conn.commit()
    conn.close()
#add an ID in database
def save_comment_id(comment_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO replied_comments(comment_id) VALUES (?)", (comment_id,))
    conn.commit()
    conn.close()

#Verify if an ID is already in my database
def is_comment_replied(comment_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM replied_comments WHERE comment_id = ?",(comment_id,))
    result=cursor.fetchone()
    conn.close()
    return result is not None #True if is there,false if is not
if __name__ == "__main__":
    setup_database()
    print("Database setup complete.")