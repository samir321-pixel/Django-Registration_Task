# Django-Registration

## Technology Stack

* Frontend
    * HTML
    * CSS
    * Bootstrap
* Backend
    * Django
* Database
    * SQLite3

## Tech Stack Involved

<div style="display: flex;justify-content: center;">

<img height="64px" width="auto" src="https://image.flaticon.com/icons/svg/919/919852.svg">
<img height="64px" width="auto" src="https://www.w3schools.com/whatis/img_css.jpg">
<img height="64px" width="auto" src="https://www.drupal.org/files/project-images/bootstrap-stack.png">
<img height="64px" width="auto" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/1200px-HTML5_logo_and_wordmark.svg.png">
<img height="64px" width="auto" src="https://twilio-cms-prod.s3.amazonaws.com/images/django-dark.width-808.png">
<div/>

<br/>
<br/>

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone git@github.com:samir321-pixel/Django-Registration.git
```

## Install Requirements:

```bash
pip install -r requirements.txt
```

## Postgres Plugin:

```bash
create a postgres container
```

```bash
create a database inside postgres,
NAME = demo
```

```bash
Provide HOST, PASSWORD, USER in Django_Registration/settings.py file
```

![image](https://user-images.githubusercontent.com/65664404/169957210-484f5f1a-3091-43ff-aec4-4fefbffe1194.png)

## Apply the migrations:

```bash
python manage.py migrate
```

## Create Superuser:

```bash
python manage.py createsuperuser
```

Add Your Name, Email & Password.

## Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **http://127.0.0.1:8000/**.

## Celery Plugin

```
Celery 4.0+ does not officially support Windows yet.
But it still works on Windows for some development/test purposes.
Use eventlet instead as below:
```

# Command 1

```bash
celery -A Django_Registration worker -l info -P eventlet
```

# Command 2

```bash
celery -A Django_Registration beat -l info
```
