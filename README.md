git clone https://github.com/sonykonda/todo-list-django.git

cd todo-list-django

python -m venv venv

venv\Scripts\activate

python manage.py makemigrations todo

python manage.py migrate

python manage.py runserver

