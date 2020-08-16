# django_project
### This is a rest-api using django in python.

Application path : ``` backend_test/assignment```

**Models used in the application** : Users & ActivityPeriod

Files Paths (for application): 
> assignment/models.py

> assignment/serializers.py

> assignment/views.py

> backend_test/urls.py

> few changes in backen_test/setting.py
 
 
**Basic Dependencies for running the API**

First create a virtual environment
>python3 -m venv env

>source env/bin/activate

Python dependencies
>pip install django

>pip install djangorestframework

>pip install djangorestframework-jsonapi

>pip install django-filter

For running the API go to the app directory

```cd backend_test```
 
 Commands to creste/setup the database
 
>python manage.py makemigrations assignment

>python manage.py migrate


**Command to run the server in localhost**
> python manage.py runserver localhost:8080


 