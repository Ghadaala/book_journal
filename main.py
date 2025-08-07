import sys
import os
import sqlite3
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit,
    QVBoxLayout, QListWidget, QListWidgetItem, QPushButton, QDateEdit
)
from PyQt5.QtCore import Qt, QDate


DB_FILE = "reviews.db"


class ReviewApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("مراجعات الكتب")
        self.editing_id = None  # ID المراجعة التي نعدلها حالياً

        self.init_db()  # إنشاء قاعدة البيانات إذا لم تكن موجودة
        self.init_ui()
        self.load_reviews()

    def init_db(self):
        """إنشاء قاعدة البيانات إذا لم تكن موجودة"""
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT,
                genre TEXT,
                date_read TEXT,
                review TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def init_ui(self):
        layout = QVBoxLayout()

        # الحقول
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("اسم الكتاب")

        self.author_input = QLineEdit()
        self.author_input.setPlaceholderText("اسم المؤلف")

        self.genre_input = QLineEdit()
        self.genre_input.setPlaceholderText("التصنيف")

        self.date_input = QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDisplayFormat("yyyy-MM-dd")
        self.date_input.setDate(QDate.currentDate())

        self.review_input = QTextEdit()
        self.review_input.setPlaceholderText("اكتب مراجعتك هنا")

        layout.addWidget(QLabel("اسم الكتاب"))
        layout.addWidget(self.title_input)

        layout.addWidget(QLabel("المؤلف"))
        layout.addWidget(self.author_input)

        layout.addWidget(QLabel("التصنيف"))
        layout.addWidget(self.genre_input)

        layout.addWidget(QLabel("تاريخ القراءة"))
        layout.addWidget(self.date_input)

        layout.addWidget(QLabel("المراجعة"))
        layout.addWidget(self.review_input)

        # زر الحفظ / التعديل
        self.save_button = QPushButton("حفظ المراجعة")
        self.save_button.clicked.connect(self.save_review)
        layout.addWidget(self.save_button)

        # قائمة عرض المراجعات
        self.review_list = QListWidget()
        self.review_list.itemClicked.connect(self.load_review_for_edit)
        layout.addWidget(self.review_list)

        self.setLayout(layout)

    def save_review(self):
        title = self.title_input.text().strip()
        author = self.author_input.text().strip()
        genre = self.genre_input.text().strip()
        date_read = self.date_input.date().toString("yyyy-MM-dd")
        review = self.review_input.toPlainText().strip()

        if not title or not review:
            return  # يمكن تحسين الرسالة لاحقاً

        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()

        if self.editing_id is None:
            # إضافة مراجعة جديدة
            c.execute("""
                INSERT INTO reviews (title, author, genre, date_read, review)
                VALUES (?, ?, ?, ?, ?)
            """, (title, author, genre, date_read, review))
        else:
            # تعديل مراجعة موجودة
            c.execute("""
                UPDATE reviews
                SET title=?, author=?, genre=?, date_read=?, review=?
                WHERE id=?
            """, (title, author, genre, date_read, review, self.editing_id))
            self.editing_id = None
            self.save_button.setText("حفظ المراجعة")

        conn.commit()
        conn.close()

        self.clear_inputs()
        self.load_reviews()

    def load_reviews(self):
        """تحميل المراجعات من قاعدة البيانات"""
        self.review_list.clear()
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("SELECT id, title, author, genre, date_read, review FROM reviews ORDER BY id DESC")
        for row in c.fetchall():
            review_id, title, author, genre, date_read, review = row
            item = QListWidgetItem(f"{title} - {author} ({genre}) | {date_read}\n{review}")
            item.setData(Qt.UserRole, review_id)
            self.review_list.addItem(item)
        conn.close()

    def load_review_for_edit(self, item):
        """تحميل المراجعة المحددة للتعديل"""
        review_id = item.data(Qt.UserRole)
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("SELECT title, author, genre, date_read, review FROM reviews WHERE id=?", (review_id,))
        row = c.fetchone()
        conn.close()

        if row:
            title, author, genre, date_read, review = row
            self.title_input.setText(title)
            self.author_input.setText(author)
            self.genre_input.setText(genre)
            self.date_input.setDate(QDate.fromString(date_read, "yyyy-MM-dd"))
            self.review_input.setText(review)
            self.editing_id = review_id
            self.save_button.setText("تحديث المراجعة")

    def clear_inputs(self):
        self.title_input.clear()
        self.author_input.clear()
        self.genre_input.clear()
        self.date_input.setDate(QDate.currentDate())
        self.review_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReviewApp()
    window.resize(500, 600)
    window.show()
    sys.exit(app.exec_())
