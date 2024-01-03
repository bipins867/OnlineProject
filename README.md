# Django User Authentication Project

This is a simple Django web application implementing user authentication features, including user registration, login, logout, and basic user profile.

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



## Follow the instructions

- cd OnlineProject
- pip install django   
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver
