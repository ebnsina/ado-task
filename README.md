## Ado - A Task managment app built with django & MySQL

#### Basic setup

- Install django and mysqlclient package to work with mysql database.

```sh
    pipenv install django
    pipenv install mysqlclient
```

- Activate shell environment

```sh
    pipenv shell
```

- Create django project

```sh
    django-admin startproject core .
```

- Create app

```sh
    python manage.py startapp task

    or

    django-admin startapp task
```

- run the app

```sh
    python manage.py runserver
```

#### Connect to database

- Create a database

```sh
    create database ado_task
```

- Connect database django with mysql

```sh
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ado_task',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        }
    }
```

- Run makemigration

```sh
    python manage.py makemigrations
```

- Run migrate

```sh
    python manage.py migrate
```

#### Setup views

- Create directory named "templates" & create a file inside "base.html"
- Create directory named "includes" & create file inside "header.html" and "footer.html"
- Create a directory named "templates" inside task app & create another folder inside templates called "task" and create a file inside that folder called "index.html"
- inside "base.html" setup this way

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Ado Task App</title>
  </head>
  <body>
    {% include "includes/header.html" %} {% block content %}{% endblock %} {%
    include "includes/footer.html" %}
  </body>
</html>
```

- inside "index.html" setup this way

```html
{% extend "base.html" %} {% block content %}{% endblock %}
```

- Make sure to setup base template directory on settings.py file

```python
TEMPLATES = [
    {
        ...
        'DIRS': [
            BASE_DIR / 'templates'
        ],
        ...
    },
]
```

#### Authentication & Authorization

- Create user app

```python
    python manage.py startapp user
```
