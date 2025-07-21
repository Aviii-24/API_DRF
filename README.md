# 🚀 API_DRF — KPA Backend Assignment

This project is a Django REST Framework (DRF) backend created for the **KPA assignment**. It includes two main API modules for managing:

- 🛞 **Wheel Specification Form**
- 🚆 **Bogie Checksheet Form**

It is built using SQLite for local development and API testing via Postman.

---

## 🔧 Features

- ✅ CRUD operations using Django REST Framework
- 🖼️ Image upload support
- 🧪 Tested using Postman
- 🔐 Admin dashboard
- 🗂️ SQLite database (default setup)

---

## 📁 Folder Structure

API_DRF/
├── api/
│ ├── migrations/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── tests.py
│ └── views.py
├── kpa_project/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── media/
├── .env
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## 🛠️ Setup Instructions

### 🔁 Clone the Repository

```bash
git clone https://github.com/your-username/API_DRF.git
cd API_DRF
🧱 Create & Activate Virtual Environment
bash
Copy
Edit
python -m venv .venv
.venv\Scripts\activate  # Windows
📦 Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🔨 Apply Migrations
bash
Copy
Edit
python manage.py migrate
👤 Create Superuser (for Admin)
bash
Copy
Edit
python manage.py createsuperuser
Enter your username, email, and password when prompted.

▶️ Run the Server
bash
Copy
Edit
python manage.py runserver
Access the app at:
http://127.0.0.1:8000
