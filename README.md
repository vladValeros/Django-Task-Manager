# Django Task Manager

A simple task management system built with Django and MySQL. In fulfillment of the requirements in CC105-Lab

The status column updates automatically based on the due date:  
- If the due date has passed, the status will be **"Overdue"**.  
- If the due date is in the future or today, the status remains **"Pending"**.  

## Features  
✔ Create, Read, Update, and Delete (CRUD) tasks.  
✔ Automatic status update based on due date.  
✔ MySQL database integration with Django.  
✔ Search functionality to find tasks by title.  
✔ Bootstrap-styled UI with a clean design.  

## Prerequisites  
Ensure you have the following installed:  
- **Python** 3.13.1  
- **Django** 5.1.7  
- **MariaDB** 11.4.5  
- **PyMySQL** 1.1.1  
- **mysqlclient** 2.2.7  

## Setup Instructions

### 1. **Create the Project Directory**  
```sh
mkdir task_manager && cd task_manager
```
### 2. Initialize a Django Project
```sh
python -m django startproject task_manager
```
### 3. Create a Virtual Environment with Pipenv
```sh
pipenv shell 
pipenv install django pymysql mysqlclient  
```
### 4. Create a Django App
```sh
cd task_manager
python manage.py startapp tasks
```
### 5. Update Settings and Configuration
Add 'tasks' to INSTALLED_APPS in settings.py.
Configure DATABASES in settings.py to use MySQL.
On SQL, create a database named "task_manager"
```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'task_manager',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

```

### 6. Make Migrations & Migrate the Database
```sh
python manage.py makemigrations
python manage.py migrate
```

### 7. Run the Development Server
```sh
python manage.py runserver
```
Visit http://127.0.0.1:8000/ to access.
