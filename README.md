# Django-2.2-Python-The-Ultimate-Web-Development-Bootcamp
"Django 2.2 &amp; Python | The Ultimate Web Development Bootcamp" Udemy course

### Workflow
#### Environment
Virtualenv: create virtual env  `>> virtualenv myvenv` `>> myvenv\Scripts\activate` `>> myvenv\Scripts\deactivate`
<br/>Django: `>>pip install django`
<br/>Static: create static folder in project main folder

#### Basic Set Up
Files: Create .gitignore in project folder  https://gitignore.io/
<br/>Database: Open postgresql and set up a new database  
`>>chcp 1252` `>> psql -U postgres postgres` `>> CREATE DATABASE producthuntdb;`
<br/>Setting: change database setting

#### Develop Set Up
Apps: create app  `>> python manage.py createapp <appname>`
<br/>Migrate: makemigrations and migrate  `>> python manage.py makemigrations` `>> python manage.py migrate`
<br/>Static Files: collect static files

#### Develop
Model: create class in model.py. Attribute: Field; Function: invoked in html
<br/>URLS: urls.py call views function and pass dictionary
<br/>Views: create functions in views.py
<br/>HTML: create .html in templates folder
