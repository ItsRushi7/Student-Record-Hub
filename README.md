# Student Record Hub

Student Record Hub is a Django-based web application for managing student records efficiently. It provides functionalities such as adding, updating, deleting, and viewing student information using an SQLite database.

## Features
- User authentication and authorization
- Add, update, delete, and view student records
- Secure and scalable

## Technologies Used
- **Backend:** Django (Python)
- **Database:** SQLite
- **Frontend:** HTML, CSS, Bootstrap

## Installation
- django 

### Prerequisites
- Python (>=3.8)
- pip (Python package manager)
- Virtual environment (optional but recommended)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/student-record-hub.git
   cd student-record-hub
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the development server:
   ```sh
   python manage.py runserver
   ```
5. Open the application in your browser:
   ```sh
   http://127.0.0.1:8000/
   ```

## Usage
- First click to sign-up page create user (username, password, email).
- login to page (username, password).
- Manage student records (add, update, delete, read).
- Access the admin panel at `/admin`.

## Project Structure
```
StdRecHub/
├── Myapp/  # Main Django app
├── __pycache__/
├── migration/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── static/
│   ├── style.css
├── StdRecHub/  # Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── urls.py
│   ├── wsgi.py
├── templates/
│   ├── edit.html
│   ├── home.html
│   ├── index.html
│   ├── signup.html
│── db.sqlite3
│── manage.py
README.md
```



