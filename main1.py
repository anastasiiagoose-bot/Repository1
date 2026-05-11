import requests
import json

pdf_url = "https://github.com/progit/progit2/releases/download/2.1.449/progit.pdf"
pdf_filename = "progit.pdf"

print(f"Починаю завантаження PDF...")
response_pdf = requests.get(pdf_url)

if response_pdf.status_code == 200:
    with open(pdf_filename, "wb") as pdf_file:
        pdf_file.write(response_pdf.content)
    print(f"Файл {pdf_filename} успішно збережено")
else:
    print(f"Помилка при завантаженні PDF: {response_pdf.status_code}")


json_url = "http://api.open-notify.org/astros.json"
json_filename = "astros.json"

print(f"Отримую дані з API")
response_json = requests.get(json_url)

if response_json.status_code == 200:
    data = response_json.json()

    with open(json_filename, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Дані успішно записані у {json_filename} з відступами")
else:
    print(f"Помилка при отриманні JSON: {response_json.status_code}")