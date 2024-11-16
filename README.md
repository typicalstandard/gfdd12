# gfdd12

#### Клониование проекта 
```
git clone https://github.com/typicalstandard/gfdd12-.git
cd gfdd12
```
#### Cоздания venv и установка зависимостей в venv
```
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```
#### Создания и настройка пользователя в БД
```
sudo -u postgres psql
CREATE DATABASE db_name;
\c db_name
CREATE USER username WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE db_name TO username;
```
#### Миграции модели
```
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```
#### Запустить проект 
```
python app.py
```


