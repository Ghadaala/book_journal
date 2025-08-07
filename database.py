import sqlite3

# إنشاء أو فتح قاعدة البيانات
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# إنشاء جدول لحفظ مراجعات الكتب
cursor.execute('''
CREATE TABLE IF NOT EXISTS book_reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT,
    date_read TEXT,
    rating INTEGER,
    review TEXT
)
''')

conn.commit()
conn.close()
