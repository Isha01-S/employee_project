# Employee Management System

A Django-based Employee Management System with APIs, Analytics, and Visualization using Chart.js.

---

## 📝 Project Overview

This project allows you to:

- Manage employees and departments.
- Record attendance and performance.
- Expose APIs using Django REST Framework (DRF).
- Visualize analytics via charts (monthly attendance, performance).
- Authenticate using Token Authentication.
- Seed database with fake Indian employee data.

---

## 📂 Folder Structure

employee_project/
├── employees/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│ └── management/commands/seed_data.py
├── attendance/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ └── urls.py
├── employee_project/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── templates/
│ ├── analytics_dashboard.html
│ ├── charts.html
│ └── performance_charts.html
├── requirements.txt
├── .env
└── README.md

## ⚙️ Setup Instructions

1. Clone the repository

git clone <your-repo-url>
cd employee_project

2. Create virtual environment & install dependencies
python -m venv env
source env/bin/activate        # Linux/Mac
env\Scripts\activate           # Windows
pip install -r requirements.txt

3. Configure environment variables

Create a .env file  and update your DB credentials:

SECRET_KEY=your_secret_key_here
DEBUG=True
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

4. Apply migrations
python manage.py makemigrations
python manage.py migrate

5. Seed the database
python manage.py seed_data


This will create:

30–50 Employees

Departments (HR, IT, Sales, Marketing, Finance)

Attendance records for last 60 days

Performance ratings for last 6 months

🚀 Running the Server
python manage.py runserver 8001


Admin: http://127.0.0.1:8001/admin/

Swagger UI: http://127.0.0.1:8001/swagger/

Analytics Dashboard: http://127.0.0.1:8001/analytics-dashboard/

🔑 Authentication

Token-based authentication for APIs.

To get token:

POST /api-token-auth/
{
  "username": "your_admin_username",
  "password": "your_password"
}


Use token in headers:

Authorization: Token YOUR_TOKEN_HERE

📌 API Endpoints
Employees
Method	Endpoint	               Description
GET	/api/employees/employees/	List all employees (with pagination, filtering, sorting)

POST	/api/employees/employees/	Create a new employee

GET	/api/employees/employees/{id}/	Retrieve employee

PUT	/api/employees/employees/{id}/	Update employee

DELETE	/api/employees/employees/{id}/	Delete employee


Departments
Method	Endpoint	                Description
GET	/api/employees/departments/	List all departments


Attendance
Method	Endpoint	                 Description
GET	/api/attendance/attendances/	List all attendance records
POST	/api/attendance/attendances/	Create attendance record


Performance
Method	Endpoint	                    Description
GET	/api/attendance/performances/	List all performance records
POST	/api/attendance/performances/	Create performance record


Analytics
Method	Endpoint	                                            Description
GET	/api/employees/employees/analytics/monthly-overview/	Monthly attendance overview for charts
GET	/api/performance-data/	Monthly average performance data for charts

📊 Visualization

Charts use Chart.js

Available at:

http://127.0.0.1:8001/attendance-chart/ → Monthly Attendance

http://127.0.0.1:8001/performance-chart/ → Monthly Performance

http://127.0.0.1:8001/analytics-dashboard/ → Both charts in one page


🧪 Testing

Use Postman or Swagger UI for testing APIs.

Use token authentication for secure endpoints.

📝 Notes

Make sure to always use plural endpoints (employees, attendances, performances) when accessing APIs.

Use /analytics-dashboard/ for combined charts.

Seed data generates  names and emails.

🧰 Tech Stack

Backend: Django 4.x, Django REST Framework

Database: PostgreSQL

Authentication: DRF Token Authentication

Visualization: Chart.js

Faker for dummy data

Swagger UI for API docs