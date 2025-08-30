# Flask Todo App with User Authentication

A simple Flask web application with user registration, login, and personal todo lists.

## Features

1. **User Registration**: New users can register with username/password
2. **User Authentication**: Login/logout functionality
3. **Personal Todo Lists**: Each user has their own todo list
4. **Bootstrap Styling**: Clean, responsive UI
5. **Selenium-Ready**: Element IDs and classes for automated testing

## Installation

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   flask run
   ```

3. Open your browser to `http://127.0.0.1:5000`

## Default User

- **Username**: admin
- **Password**: admin

## Usage

1. **First Time**: Visit the app and register a new account
2. **Login**: Use your credentials to access your dashboard
3. **Add Tasks**: Use the input field and "Add Task" button
4. **View Tasks**: All your tasks are displayed in a list
5. **Logout**: Click logout to end your session

## File Structure

```
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
└── templates/
    ├── login.html        # Login page
    ├── register.html     # Registration page
    └── dashboard.html    # Todo dashboard
```

## Selenium Element IDs

For automated testing, the following element IDs are available:

### Login Page (`/login`)
- Username field: `id="username"`
- Password field: `id="password"`  
- Login button: `id="login-btn"`

### Register Page (`/register`)
- Username field: `id="username"`
- Password field: `id="password"`
- Confirm password field: `id="confirm_password"`
- Register button: `id="register-btn"`

### Dashboard Page (`/dashboard`)
- Task input field: `id="task-input"`
- Add task button: `id="add-task-btn"`
- Task list items: `class="task-item"`

## Notes

- User data and tasks are stored in memory only
- Each user has their own separate task list
- Data is lost when the application restarts
- Passwords are stored in plain text (not suitable for production)
