# Django TODO Application

A simple yet functional TODO application built with Django that allows users to create, edit, delete, and manage TODO items with due dates and resolution status.

## Features

- **Create TODOs**: Add new TODO items with title, description, and optional due date
- **Edit TODOs**: Update existing TODO items
- **Delete TODOs**: Remove TODO items with confirmation
- **Mark as Resolved**: Toggle TODO items between pending and resolved status
- **Due Dates**: Assign and track due dates for TODO items
- **Responsive UI**: Clean and simple user interface

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

### 1. Clone or navigate to the project directory

```bash
cd /Users/tongaimutengwa/Projects/TODO_APP
```

### 2. Create and activate a virtual environment

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Django

```bash
pip install django
```

## Setup

### 1. Apply database migrations

```bash
python manage.py migrate
```

### 2. (Optional) Create a superuser for admin access

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

## Running the Application

### Start the development server

```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000/**

### Access the admin panel (optional)

Navigate to **http://127.0.0.1:8000/admin/** and log in with your superuser credentials.

## Running Tests

The application includes comprehensive tests covering models and views.

### Run all tests

```bash
python manage.py test
```

### Run tests with verbose output

```bash
python manage.py test --verbosity=2
```

### Test coverage includes:
- TODO model creation and validation
- Home page display
- Creating TODOs
- Editing TODOs
- Deleting TODOs
- Toggling resolved status
- Error handling for non-existent items

## Project Structure

```
TODO_APP/
├── manage.py                 # Django management script
├── README.md                 # This file
├── db.sqlite3               # SQLite database (created after migrations)
├── todoproject/             # Main project directory
│   ├── __init__.py
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL configuration
│   ├── asgi.py              # ASGI configuration
│   └── wsgi.py              # WSGI configuration
├── todos/                   # TODO app directory
│   ├── __init__.py
│   ├── admin.py             # Admin configuration
│   ├── apps.py              # App configuration
│   ├── models.py            # TODO model definition
│   ├── views.py             # View functions
│   ├── urls.py              # App URL patterns
│   ├── tests.py             # Test cases
│   ├── migrations/          # Database migrations
│   └── templates/           # HTML templates
│       └── todos/
│           ├── base.html    # Base template
│           ├── home.html    # Home page
│           ├── create.html  # Create TODO form
│           ├── edit.html    # Edit TODO form
│           └── delete.html  # Delete confirmation
└── venv/                    # Virtual environment (not in version control)
```

## Usage

### Creating a TODO

1. Navigate to the home page
2. Click "Create New TODO"
3. Fill in the title (required), description (optional), and due date (optional)
4. Click "Create TODO"

### Editing a TODO

1. On the home page, find the TODO you want to edit
2. Click the "Edit" button
3. Update the fields as needed
4. Click "Save Changes"

### Deleting a TODO

1. On the home page, find the TODO you want to delete
2. Click the "Delete" button
3. Confirm the deletion

### Marking a TODO as Resolved

1. On the home page, find the TODO you want to mark
2. Click "Mark as Resolved" (or "Mark as Pending" if already resolved)
3. The TODO status will update immediately

## Database Model

### TODO Model

| Field       | Type          | Description                           |
|-------------|---------------|---------------------------------------|
| id          | AutoField     | Primary key (auto-generated)          |
| title       | CharField     | TODO title (max 200 characters)       |
| description | TextField     | Detailed description (optional)       |
| due_date    | DateField     | Due date (optional)                   |
| resolved    | BooleanField  | Resolution status (default: False)    |
| created_at  | DateTimeField | Creation timestamp (auto-generated)   |
| updated_at  | DateTimeField | Last update timestamp (auto-updated)  |

## Homework Questions & Answers

This project was built as part of a Django homework assignment. Here are the answers:

1. **Install Django**: `pip install django`
2. **Project and App**: Edit `settings.py` to add the app to INSTALLED_APPS
3. **Django Models**: `Run migrations` (makemigrations and migrate)
4. **TODO Logic**: Implement in `views.py`
5. **Templates**: Register in `TEMPLATES['DIRS']` in project's settings.py (or use APP_DIRS)
6. **Tests**: Run with `python manage.py test`

## Technologies Used

- **Django 5.2.8**: Web framework
- **SQLite**: Database (default Django database)
- **Python 3**: Programming language
- **HTML/CSS**: Frontend templates and styling

## Development

### Adding new features

1. Update models in `todos/models.py` if needed
2. Create and apply migrations: `python manage.py makemigrations && python manage.py migrate`
3. Add views in `todos/views.py`
4. Create URL patterns in `todos/urls.py`
5. Create templates in `todos/templates/todos/`
6. Write tests in `todos/tests.py`
7. Run tests to ensure everything works: `python manage.py test`

## Troubleshooting

### Server won't start
- Ensure the virtual environment is activated
- Check that Django is installed: `pip list | grep Django`
- Verify migrations are applied: `python manage.py migrate`

### Tests failing
- Ensure all migrations are applied
- Check database permissions
- Run tests with verbose output for more details: `python manage.py test --verbosity=2`

### Page not found (404)
- Verify URL patterns in `todos/urls.py` and `todoproject/urls.py`
- Check that the app is registered in `INSTALLED_APPS` in settings.py

## License

This project is for educational purposes as part of a AI Assisted Development homework assignment.

## Author

Created as part of an AI Assisted Development course homework.
