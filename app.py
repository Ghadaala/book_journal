from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class BookReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    year = db.Column(db.String(4))  # سنة النشر كنص
    reading_date = db.Column(db.String(20))  # تاريخ القراءة كنص
    review_text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<BookReview {self.title}>"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_review', methods=['POST'])
def add_review():
    title = request.form['title'].strip()
    author = request.form['author'].strip()
    year = request.form['year'].strip()
    reading_date = request.form['reading_date'].strip()
    review_text = request.form['review_text'].strip()

    if not title or not author or not review_text:
        # يمكنك إضافة رسائل خطأ أو إعادة التوجيه مع تنبيه
        return redirect(url_for('index'))

    new_review = BookReview(
        title=title,
        author=author,
        year=year,
        reading_date=reading_date,
        review_text=review_text
    )
    db.session.add(new_review)
    db.session.commit()

    return redirect(url_for('reviews'))

@app.route('/reviews')
def reviews():
    all_reviews = BookReview.query.order_by(BookReview.id.desc()).all()
    return render_template('reviews.html', reviews=all_reviews)

@app.route('/review/<int:review_id>')
def review_detail(review_id):
    review = BookReview.query.get_or_404(review_id)
    return render_template('review_detail.html', review=review)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
