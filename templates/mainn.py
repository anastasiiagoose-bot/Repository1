import smtplib
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader
from pywebio import start_server
from pywebio.input import input_group, input
from pywebio.output import put_success, put_error


SMTP_SERVER, SMTP_PORT = "smtp.gmail.com", 587
SENDER_EMAIL = "anastasiiagoose@gmail.com"  #пошта
EMAIL_TOKEN = "your_app_password_token"  #токен


def send_html_email(recipient: str, subject: str, html_content: str) -> None:
    """Формує та відправляє HTML-лист."""
    msg = MIMEText(html_content, "html", "utf-8")
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = recipient

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, EMAIL_TOKEN)
        server.sendmail(SENDER_EMAIL, recipient, msg.as_string())


def app_logic() -> None:
    """Збір даних, обробка, рендеринг шаблону та відправка."""
    # Отримання даних через PyWebIO
    data = input_group("Форма обробки рядка", [
        input("Введіть ваше ім'я:", name="username", required=True),
        input("Введіть рядок:", name="user_string", required=True),
        input("Ваш Email:", name="email", required=True)
    ])

    # Обробка стрічки
    cleaned_str = data["user_string"].strip()

    # Генерація листа через
    env = Environment(loader=FileSystemLoader("templates"))
    html_body = env.get_template("string.html").render(
        username=data["username"],
        cleaned_string=cleaned_str,
        string_length=len(cleaned_str)
    )

    # Відправка та результат
    try:
        send_html_email(data["email"], "Результат обчислення", html_body)
        put_success(f"Лист успішно надіслано на {data['email']}")
    except Exception as e:
        put_error(f"Помилка відправки: {e}")


if __name__ == "__main__":
    start_server(app_logic, port=8080)