# Django Students CRUD

Full CRUD implementation for a **Student** model in Django, using **ModelForms** and **base templates**.

## Features
- Create new students (with fields: first name, last name, nickname, bio)
- List all students
- View student detail (including bio)
- Edit student info (using ModelForm with instance binding)
- Delete student
- Base layout with navigation (Home, New Student)

## Tech Stack
- Python 3, Django
- SQLite (default)

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://localhost:8000/students/
