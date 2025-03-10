# Django Task Manager

A simple task management system built with Django and MySQL. In fulfillment of the requirements in CC105-Lab

A Django-based Task Manager with CRUD functionality. The status column updates automatically based on the due date:  
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

