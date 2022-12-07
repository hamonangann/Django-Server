rpl bkn jarkom

## What you need
- Python
- Pip
- PostgreSQL server running

## How to start
- git clone https://github.com/hamonangann/jarkomolla
- python -m venv venv
- venv\Scripts\activate
- cd jarkomolla
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver

## Debug

If cannot load database, open your Postgre Client and create new database 'jarkomolla'

e.g open psql (shell) and run 'CREATE DATABASE jarkomolla'

## Django Template

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/GB6Eki?referralCode=U5zXSw)
