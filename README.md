# Django User Authentication Project

This is a simple Django web application implementing user authentication features, including user registration, login, logout, and basic user profile.

Video Demonstration :- https://drive.google.com/file/d/1AmhwQl9yc3iFil5TUzpxj9eyxeBBQBJt/view?usp=sharing

## Features

- User registration (sign-up) with fields: Username, Email, Password, Confirm Password.
- User login with fields: Username or Email, Password.
- Secure password storage using Django's password hashing.
- Session management for user authentication.
- Logout functionality.
- Basic user profile page displaying user information.
- SQLite database for storing user information.
- Form validation for registration and login.

## Project Structure

The project is organized into a Django project and a single app. The main components are:

- **myproject/**: Django project folder.
- **myapp/**: Django app folder containing user authentication views, templates, and forms.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/bipins867/OnlineProject.git

2. Navigate to the project folder:

   ```bash
   cd OnlineProject

3. Install dependencies:

   ```bash
   pip install django

4. Run migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. Create a superuser(admin):

   ```bash
   python manage.py createsuperuser

6. Run the development server
   
   ```bash
   python manage.py runserver


The application will be accessible at http://127.0.0.1:8000/login/



## Usage

- Access the registration page: http://127.0.0.1:8000/register/
- Register a new user with a unique username and email.
- Access the login page: http://127.0.0.1:8000/login/
- Log in using the registered username or email.
- After login, you will be redirected to the dashboard: http://127.0.0.1:8000/dashboard/
- Access the user profile: http://127.0.0.1:8000/profile/
- Logout using the "Logout" link.


## Notes

- This project uses Django's built-in authentication system, including UserCreationForm and AuthenticationForm.
- Passwords are securely stored using Django's password hashing.
- Session management is handled by Django's authentication system.
