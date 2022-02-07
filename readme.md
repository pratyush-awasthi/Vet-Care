This Vet Care is a Static Animal Blogging Website. 

The website use Django Framework for backend processes and SQLite as the database.

There are several different tables in the database for keeping record of the blogs.

Forms are made using Crispy Forms. 

The whole website is made using HTML 5 and Bootstrap.

This server currently does not have login functionality.

To run the server on the localhost You need to write 
```
    python manage.py runserver
```

Inorder to create a superuser for the admin portal you need to write
```
    python manage.py createsuperuser
```

Inorder to save modifications done in the database like the changes in the table format or anything else then you need to write
```
    python manage.py migrate
```

If you want to create a new app in the existing server then write
```
    python manage.py startapp "appname"
```

Requirements :

1) Python
2) Django
3) Django Extensions
4) Django Crispy Forms
5) Crispy Forms Boostrap5

### How to setup a New Django Project?


Check for Python
```
    python --version
```

Install Django
```
    pip install django
```

Install Django Extensions
```
    pip install django-extensions
```

Install Django Crispy Forms
```
    pip install django-crispy-forms
```

Install Crispy Bootstrap 5
```
    pip install crispy-bootstrap5
```

If you want to add login through social authentication then
Install Social Auth App Django
```
    pip install social-auth-app-django
```

Install Pillow
```
    pip install pillow
```

Then write the following line
```
    python -m django startproject "projectname"
```

Then create the Database by typing
```
    python manage.py migrate
```