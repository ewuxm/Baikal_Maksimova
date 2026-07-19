# Проект "Байкал" - Безопасный SQL Runner

## Описание
Простой Python-скрипт для безопасного выполнения SELECT-запросов к PostgreSQL.

## Как запустить

1. Клонируйте репозиторий
2. Создайте виртуальное окружение: python -m venv venv
3. Активируйте его:
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`
4. Установите зависимости: pip install -r requirements.txt
5. Создайте файл `.env` в папке с проектом и укажите свои данные для подключения к БД.
DB_HOST=localhost
DB_PORT=5432
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=ваш_пароль
6. Запустите: python main.py
