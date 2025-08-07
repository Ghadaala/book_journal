# 📚 برنامج إدارة قراءاتي الشخصية

برنامج مكتبي بسيط باستخدام Flask يسمح لك بتسجيل مراجعاتك وانطباعاتك عن الكتب التي تقرأها، مع إمكانية تصفحها لاحقًا.

---

## 🚀 تشغيل البرنامج

### 1. تهيئة بيئة العمل (أول مرة فقط):
```bash
python -m venv venv
venv\Scripts\activate  # على ويندوز
pip install -r requirements.txt
ملاحظة: يمكنك إنشاء requirements.txt بالأمر:

pip freeze > requirements.txt


2. تشغيل التطبيق:

set FLASK_APP=app.py  # على ويندوز
set FLASK_ENV=development
flask run
ثم افتح المتصفح على:
http://127.0.0.1:5000/

