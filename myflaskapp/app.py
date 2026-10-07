from flask import Flask
import mysql.connector  # Додаємо імпорт бібліотеки для роботи з MySQL

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        # Спроба підключитися до бази даних. 
        # Саме тут ми прописуємо host="db" замість "localhost"
        mydb = mysql.connector.connect(
            host="db",
            user="root",
            password="1234",
            database="mysql" # Стандартна системна БД, яка вже існує в контейнері
        )
        mydb.close()
        return "<h1>Hello from Flask! Підключення до БД 'db' успішне!</h1>"
    except Exception as e:
        return f"<h1>Hello from Flask! Помилка підключення: {e}</h1>"

if __name__ == "__main__":
    # Цей рядок відповідає за веб-сервер і обов'язково залишається 0.0.0.0
    app.run(host="0.0.0.0", port=5000)