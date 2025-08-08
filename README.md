# 📚 برنامج إدارة قراءاتي الشخصية-Book Journal

# وصف المشروع

برنامج مكتبي بسيط تم تطويره باستخدام إطار عمل Flask و SQLite. يهدف إلى مساعدة المستخدمين في تسجيل مراجعاتهم وانطباعاتهم عن الكتب التي يقرؤونها، مع إمكانية تصفحها وتعديلها بسهولة.

# المميزات:

* إضافة مراجعة جديدة: إمكانية إدخال اسم الكتاب، المؤلف، وتصنيف المراجعة.
* قاعدة بيانات محلية: حفظ جميع البيانات في ملف قاعدة بيانات SQLite (reviews.db)، مما يضمن سهولة الإدارة والتنظيم.
* واجهة مستخدم بسيطة: تصميم واضح وسهل الاستخدام.
* وصول مباشر لقاعدة البيانات: يمكن للمستخدمين الوصول إلى جميع المراجعات التي قاموا بإدخالها في قاعدة البيانات على شكل جداول باستخدام برنامج خارجي مثل DB Browser for SQLite.يتم تحميل البرنامج على الرابط : [https://sqlitebrowser.org/](https://sqlitebrowser.org/)

<img width="91" height="149" alt="image" src="https://github.com/user-attachments/assets/31c02140-481e-451f-b00d-eba681e8da60" />


# دليل المطورين: البدء:

اتبع هذه الخطوات لتجهيز بيئة التطوير وتشغيل البرنامج.

## 1. المتطلبات
تأكد من تثبيت Python 3.x على جهازك.

## 2. إعداد بيئة العمل
يفضل استخدام بيئة افتراضية (Virtual Environment) لعزل مكتبات المشروع.

إنشاء البيئة الافتراضية
python -m venv venv

تفعيل البيئة الافتراضية
على نظام Windows
venv\Scripts\activate
 على نظام macOS و Linux
source venv/bin/activate

<img width="863" height="272" alt="image" src="https://github.com/user-attachments/assets/ec232923-2033-439c-9e8f-73da0ecab798" />


## 3. تثبيت المكتبات الضرورية
بمجرد تفعيل البيئة الافتراضية، قم بتثبيت جميع المكتبات المذكورة في ملف requirements.txt:

pip install -r requirements.txt

## 4. هيكل المشروع
للمساعدة في فهم هيكل الملفات والمجلدات:

<img width="974" height="329" alt="image" src="https://github.com/user-attachments/assets/f18debba-9d16-4e8e-aa68-e60a237fc4e3" />


.
├── instance/               # مجلد خاص ببيانات التطبيق (مثل قاعدة البيانات)
├── reviews.db              # ملف قاعدة بيانات SQLite
├── static/                 # ملفات CSS, JS, صور
├── templates/              # قوالب HTML
├── venv/                   # مجلد البيئة الافتراضية
├── app.py                  # الملف الرئيسي لتشغيل تطبيق Flask
├── database.py             # دوال للتعامل مع قاعدة البيانات
├── requirements.txt        # قائمة المكتبات المطلوبة
├── README.md               # هذا الملف
└── ...

## 5. تشغيل التطبيق
يمكنك تشغيل التطبيق باستخدام أوامر Flask:

# تحديد ملف التطبيق
# على نظام Windows
set FLASK_APP=app.py

# على نظام macOS و Linux
export FLASK_APP=app.py

# تشغيل التطبيق
flask run


<img width="893" height="288" alt="image" src="https://github.com/user-attachments/assets/f15c76f5-a115-4369-bfcb-73dea2bdf0ab" />


بعد تشغيل الأمر، سيظهر لك عنوان URL في الطرفية. افتح المتصفح على:
http://127.0.0.1:5000/




# المساهمة:

نرحب بمساهماتك لتحسين هذا المشروع! يمكنك:

فتح مشكلة (Issue) للإبلاغ عن خطأ أو اقتراح ميزة جديدة.

إنشاء طلب سحب (Pull Request) لإضافة تعديلاتك.
-----------------------------------------------
# Book JournalProject
Description: A simple desktop application developed using the Flask framework and SQLite. Its purpose is to help users record their reviews and impressions of the books they read, with the ability to browse and edit them easily.
Features:
* Add New Review: Ability to enter the book's name, author, and review rating.
* Local Database: All data is saved in a local SQLite database file (reviews.db), ensuring easy management and organization.
* Simple User Interface: A clean and easy-to-use design.
* Direct Database Access: Users can access all their entered reviews in a table format using an external program like DB Browser for SQLite.

# Developer Guide:Getting Started

Follow these steps to set up the development environment and run the application:

## 1. PrerequisitesMake sure you have Python 3.x installed on your machine.

## 2.  Setting up the Virtual Environment
   It is recommended to use a virtual environment to isolate the project's libraries.
 Create the virtual environment
python -m venv venv

 Activate the virtual environment
On Windows
venv\Scripts\activate
On macOS and Linux
source venv/bin/activate
<img width="794" height="272" alt="image" src="https://github.com/user-attachments/assets/d4fd66ed-1ba3-4523-aa29-0c1ceb989230" />

## 3. Installing DependenciesOnce the virtual environment is active, install all the libraries listed in the requirements.txt file:
pip install -r requirements.txt
<img width="578" height="97" alt="image" src="https://github.com/user-attachments/assets/51e3e4de-c3cd-4955-9bea-72d7dac88c7e" />

## 4. Project StructureTo help you understand the file and folder structure:.

├── instance/               # Folder for application data (like the database)
├── reviews.db              # SQLite database file
├── static/                 # CSS, JS, images
├── templates/              # HTML templates
├── venv/                   # Virtual environment folder
├── app.py                  # The main Flask application file
├── database.py             # Functions for handling the database
├── requirements.txt        # List of required libraries
├── README.md               # This file
└── ...

<img width="926" height="348" alt="image" src="https://github.com/user-attachments/assets/80e4f736-3fdf-44ea-aa50-f3ad7be0d3d7" />

## 5. Running the ApplicationYou can run the application using Flask commands:# Specify the application file
 On Windows
set FLASK_APP=app.py

On macOS and Linux
export FLASK_APP=app.py

 Run the application
flask run
<img width="840" height="285" alt="image" src="https://github.com/user-attachments/assets/449fb4d1-e476-4fb3-a87a-29f4cb1272f4" />

After running the command, a URL will appear in the terminal. Open your browser to:http://127.0.0.1:5000/
# Contribution
We welcome your contributions to improve this project! You can:
* Open an Issue to report a bug or suggest a new feature.
* Create a Pull Request to add your changes.
