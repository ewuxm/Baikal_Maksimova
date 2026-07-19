import os
import re
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def main():
    print("=" * 50)
    print("БЕЗОПАСНЫЙ SQL RUNNER")
    print("Проект БАЙКАЛ")
    print("=" * 50)

    # 1. Подключаемся к базе данных
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        print("Подключение к PostgreSQL успешно!")
    except Exception as e:
        print(f"Ошибка подключения: {e}")
        return

    # 2. Запрашиваем SQL-запрос у пользователя
    sql = input("\nВведите SQL-запрос: ").strip()

    if not sql:
        print("Запрос не может быть пустым")
        conn.close()
        return

    # 3. Проверяем, что это SELECT (убираем комментарии)
    cleaned = re.sub(r'--.*?$', '', sql, flags=re.MULTILINE)
    cleaned = re.sub(r'/\*.*?\*/', '', cleaned, flags=re.DOTALL)
    cleaned = cleaned.strip().upper()

    # Если запрос не начинается с SELECT — блокируем
    if not cleaned.startswith("SELECT"):
        print("Ошибка: разрешены только SELECT-запросы")
        conn.close()
        return

    # 4. Добавляем LIMIT 5, если его нет
    if not re.search(r'\bLIMIT\b', sql, re.IGNORECASE):
        sql += " LIMIT 5"
        print("Добавлен LIMIT 5")

    # 5. Выполняем запрос и выводим результат
    try:
        with conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()
            colnames = [desc[0] for desc in cur.description] if cur.description else []

            if not rows:
                print("Запрос вернул 0 строк.")
            else:
                # Простой вывод
                print("\nРезультаты:")
                print(" | ".join(colnames))
                print("-" * 50)

                for row in rows:
                    print(" | ".join(str(val) for val in row))

                print(f"\n Всего строк: {len(rows)}")

    except Exception as e:
        print(f" Ошибка выполнения запроса: {e}")

    # 6. Закрываем соединение
    conn.close()
    print(" Соединение закрыто")

if __name__ == "__main__":
    main()
