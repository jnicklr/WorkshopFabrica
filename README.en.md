# Workshop - Software Factory

Project developed as a challenge for the UNIPE Software Factory selection process, the system was built using the Django REST framework, and it consists of a process for enrolling in a university.

## Technologies Used:

* [Python](https://www.python.org/): programming language
* [Django REST](https://www.django-rest-framework.org/): web framework
* [PostgreSQL](https://www.postgresql.org/): database

## How to Run:

### **1. Install `Python` on your machine, via [this link](https://www.python.org/)**

### **2. Clone [this repository](https://github.com/jnicklr/WorkshopFabrica.git) to your machine:**

* Create a folder on your computer for this program
* Open the `git bash` or `terminal` inside that folder
* Copy the [repository URL](https://github.com/jnicklr/WorkshopFabrica.git)
* Type `git clone <copied URL>` and press `enter`

### **3. Create a virtual environment:**

* Open your code editor's terminal and type `python -m venv "venv-name"`
* Activate your virtual environment `venv-name\Scripts\activate` (Windows)
* Activate your virtual environment `source venv-name/bin/activate` (Unix/MacOS)
* If you can't activate it, first allow scripts to be executed in the project by typing `Set-executionPolicy -Scope Process -ExecutionPolicy Bypass` in the terminal, then try activating it again.

### **4. Install project requirements via the terminal:**

* Open your code editor's terminal and type `pip install -r requirements.txt`

### **5. Configure your database and apply migrations:**
* Type `python manage.py migrate`

### **6. Run the program via the terminal:**
* Type `python manage.py runserver`

## About the APIs and how to access them:

You can access the API by appending any of the routes listed below to the URL (after starting the server), for example, `http://127.0.0.1:8000/student/` will give you access to the student API. Through the URL, you can perform all HTTP methods such as GET, POST, PUT, and DELETE. To use the PUT and DELETE methods, you need to specify the index/id of the data to be manipulated at the end of the URL, like `http://127.0.0.1:8000/student/1/`. The applications have pagination to determine the amount of data that will appear on the page. If you want to change this, just put the desired limit at the end of the URL as I will show `http://127.0.0.1:8000/student/?limit=x`, where x indicates how many can appear.

**API Routes:**
* `/teacher/`
* `/subject/`
* `/content/`
* `/course/`
* `/student/`
* `/enrollment/`

**Entity Relationships:**

![image](https://github.com/jnicklr/WorkshopFabrica/assets/102833896/4b0ab933-d76e-45d9-be74-3c01d2a2b93e)
