# TickIt - Task Management Application

A modern, feature-rich task management application built with Django that helps users organize, prioritize, and track their tasks efficiently.

## 🚀 Features

### Core Functionality
- **Task Management**: Create, edit, delete, and view tasks
- **Priority System**: Set tasks as Low, Medium, or High priority
- **Due Date Tracking**: Set and track due dates for tasks
- **Completion Status**: Mark tasks as completed with automatic timestamp
- **Overdue Detection**: Automatic detection of overdue tasks
- **User Authentication**: Secure user registration and login system

### Advanced Features
- **Filtering**: Filter tasks by status (pending/completed)
- **Sorting**: Sort tasks by priority, due date, or creation date
- **Search**: Search tasks by title and description
- **Responsive Design**: Modern, mobile-friendly interface
- **REST API**: Full API support for mobile apps and integrations

### User Experience
- **Intuitive Interface**: Clean and user-friendly design
- **Real-time Updates**: AJAX-powered task completion toggling
- **Success Messages**: User feedback for all actions
- **Responsive Layout**: Works seamlessly on desktop and mobile devices

## 🛠️ Technology Stack

- **Backend**: Django 5.2.3
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **API**: Django REST Framework
- **Authentication**: JWT Authentication
- **Documentation**: DRF Spectacular (OpenAPI/Swagger)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Python Version**: 3.8+

## 📋 Prerequisites

Before running this application, make sure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)
- Git

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd tickit
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations
```bash
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## 📁 Project Structure

```
tickit/
├── config/                 # Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py         # Main settings file
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py
├── tasks/                  # Main application
│   ├── __init__.py
│   ├── admin.py           # Django admin configuration
│   ├── api_views.py       # REST API views
│   ├── apps.py
│   ├── forms.py           # Form definitions
│   ├── migrations/        # Database migrations
│   ├── models.py          # Task model definition
│   ├── serializers.py     # API serializers
│   ├── templates/         # Task-specific templates
│   ├── tests.py
│   ├── urls.py            # Task app URLs
│   └── views.py           # View functions
├── templates/             # Global templates
│   ├── base.html          # Base template
│   └── registration/      # Auth templates
├── manage.py
└── README.md
```

## 🗄️ Database Schema

### Task Model
- `title` (CharField): Task title (max 200 characters)
- `description` (TextField): Optional task description
- `created_at` (DateTimeField): Task creation timestamp
- `updated_at` (DateTimeField): Last update timestamp
- `due_date` (DateTimeField): Optional due date
- `priority` (CharField): Priority level (low/medium/high)
- `completed` (BooleanField): Completion status
- `completed_at` (DateTimeField): Completion timestamp
- `user` (ForeignKey): Associated user

## 🌐 API Documentation

### Authentication
The API uses JWT (JSON Web Token) authentication. Include the token in the Authorization header:
```
Authorization: Bearer <your-jwt-token>
```

### Endpoints

#### User Registration
- **POST** `/api/register/`
- **Description**: Register a new user
- **Request Body**:
  ```json
  {
    "username": "string",
    "email": "string",
    "password": "string"
  }
  ```

#### Task Management
- **GET** `/api/tasks/` - List all tasks for authenticated user
- **POST** `/api/tasks/` - Create a new task
- **GET** `/api/tasks/{id}/` - Get specific task details
- **PUT** `/api/tasks/{id}/` - Update a task
- **DELETE** `/api/tasks/{id}/` - Delete a task

#### Task Completion
- **POST** `/api/tasks/{id}/mark_complete/` - Mark task as complete

### Query Parameters
- `filter`: Filter tasks by status (`completed`, `pending`)
- `ordering`: Sort tasks (`priority`, `due_date`, `created_at`)
- `search`: Search in title and description

### Example API Usage

```bash
# Get all tasks
curl -H "Authorization: Bearer <token>" http://localhost:8000/api/tasks/

# Create a new task
curl -X POST -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"title":"New Task","description":"Task description","priority":"high"}' \
  http://localhost:8000/api/tasks/

# Filter completed tasks
curl -H "Authorization: Bearer <token>" \
  http://localhost:8000/api/tasks/?filter=completed
```

## 🎨 Web Interface

### Available Pages
- **Home** (`/`): Task list with filtering and sorting options
- **Login** (`/login/`): User authentication
- **Register** (`/register/`): New user registration
- **Create Task** (`/task/new/`): Add new task form
- **Task Detail** (`/task/{id}/`): View task details
- **Edit Task** (`/task/{id}/edit/`): Modify existing task
- **Delete Task** (`/task/{id}/delete/`): Confirm task deletion

### Features
- **Responsive Design**: Works on all device sizes
- **Real-time Updates**: AJAX-powered interactions
- **User Feedback**: Success/error messages
- **Intuitive Navigation**: Easy-to-use interface

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root for production settings:

```env
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=your-domain.com
DATABASE_URL=postgresql://user:password@localhost/dbname
```

### Database Configuration
The application is configured to use SQLite by default. For production, update the database settings in `config/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

## 🚀 Deployment

### Production Checklist
1. Set `DEBUG = False` in settings
2. Configure a production database (PostgreSQL recommended)
3. Set up static file serving
4. Configure HTTPS
5. Set up proper logging
6. Use environment variables for sensitive data

### Deployment Options
- **Heroku**: Easy deployment with PostgreSQL add-on
- **DigitalOcean**: App Platform or Droplet
- **AWS**: Elastic Beanstalk or EC2
- **Docker**: Containerized deployment

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/your-repo/tickit/issues) page
2. Create a new issue with detailed information
3. Contact the development team

## 🔮 Future Enhancements

- [ ] Task categories/tags
- [ ] File attachments
- [ ] Task sharing/collaboration
- [ ] Email notifications
- [ ] Calendar integration
- [ ] Mobile app
- [ ] Dark mode theme
- [ ] Task templates
- [ ] Time tracking
- [ ] Progress reports

---

**TickIt** - Organize your life, one task at a time! 🎯 