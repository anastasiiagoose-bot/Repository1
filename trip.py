
from pywebio import start_server

from pywebio.input import input, select, slider, NUMBER

from pywebio.output import put_text, put_table, put_error, put_success


import math


def trip_organizer():
    put_text("Організатор шкільної поїздки")

    # Введення даних
    num_students = input("Введіть кількість учнів:", type=NUMBER)



    # Перевірка
    if num_students <= 0:
        put_error("Помилка: Кількість учнів має бути більшою за 0!")
        return



    num_teachers = input("Введіть кількість вчителів:", type=NUMBER)
    transport = select("Оберіть тип транспорту:", ["Автобус", "Поїзд"])
    num_days = slider("Оберіть кількість днів:", min_value=0, max_value=14, step=1)



    # Розрахунки
    total_people = num_students + num_teachers



    # Розрахунок
    bus_count = 0



    if transport == "Автобус":
        bus_count = math.ceil(total_people / 40)
        transport_cost = bus_count * 5000
    else:
        # Поїзд
        transport_cost = total_people * 300



    # Розрахунок проживання
    live_cost = total_people * 400 * num_days



    # Загальна сума
    total_price = transport_cost + live_cost



    # Знижка 10%
    discount = 0
    if total_people > 30:
        discount = total_price * 0.1
        total_price = discount



    # Виведення результату
    put_text("Результати розрахунку")



    results = [
        ["Параметр:", "Значення:"],
        ["Загальна кількість людей:", total_people],
        ["Тип транспорту:", transport],
        ["Вартість транспорту:", f"{transport_cost} грн"],
        ["Вартість проживання:", f"{live_cost} грн"],
        ["Знижка (10%):", f"{discount} грн" if discount > 0 else "Немає"],
        ["ЗАГАЛЬНА СУМА:", f"{total_price} грн"]
    ]



    if bus_count > 0:
        results.insert(3, ["Необхідно автобусів:", bus_count])



    put_table(results)
    put_success("Розрахунок завершено успішно!")

if __name__ == '__main__':
    start_server(trip_organizer, port=8080, auto_open_webbrowser=True)
