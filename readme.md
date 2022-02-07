This Vet Care is a Static Animal Blogging Website. 

The website use Django Framework for backend processes and SQLite as the database.

There are several different tables in the database for keeping record of the blogs.

Forms are made using Crispy Forms. 

The whole website is made using HTML 5 and Bootstrap.

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
