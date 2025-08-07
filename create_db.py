import sqlite3

DB_PATH = "reviews.db"

# الاتصال بقاعدة البيانات أو إنشاؤها
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

# إنشاء جدول المراجعات إذا لم يكن موجودًا
c.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    genre TEXT,
    date TEXT,
    review TEXT NOT NULL,
    rating INTEGER,
    tag TEXT,
    shared BOOLEAN DEFAULT 0
)
""")

conn.commit()
conn.close()

print(f"✅ تم إنشاء/تحديث قاعدة البيانات: {DB_PATH}")

