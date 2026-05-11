import csv

file_path = 'airport-codes_csv.csv'

try:
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')

        print("Список аеропортів України:")
        print("-" * 30)

        counter = 0
        for row in reader:
            if row['iso_country'] == 'UA':
                print(row['name'])
                counter += 1

        print("-" * 30)
        print(f"Всього знайдено: {counter}")

except FileNotFoundError:
    print(f"Помилка: Файл {file_path} не знайдено. Перевірте його наявність у папці з проектом.")
except KeyError:
    print("Помилка: Не знайдено колонку 'iso_country' або 'name'. Перевірте структуру CSV.")