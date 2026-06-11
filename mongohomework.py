import pymongo
from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://anastasiiagoose_db_user:YwunikfN6o3QMvKg@cluster0.mongodb.net/?retryWrites=True&w=majority"

try:
    client = MongoClient(CONNECTION_STRING)
    client.admin.command('ping')
    print("Успішно підключено до MongoDB Atlas!\n")
except Exception as e:
    print(f"Помилка підключення: {e}")
    exit()

db = client["school_library"]
collection = db["books"]

collection.delete_many({})

game_of_thrones = {
    "title": "Гра престолів",
    "price": 450,
    "year": 2015,
    "pages": 800
}
collection.insert_one(game_of_thrones)
print("Книгу 'Гра престолів' успішно додано.")

school_books = [
    {"title": "Алгебра", "class_level": 7, "pages": 250, "year": 2022},
    {"title": "Геометрія", "class_level": 8, "pages": 220, "year": 2021},
    {"title": "Історія України", "class_level": 5, "pages": 180, "year": 2022},
    {"title": "Українська література", "class_level": 6, "pages": 310, "year": 2020},
    {"title": "Фізика", "class_level": 9, "pages": 280, "year": 2022},
    {"title": "Біологія", "class_level": 7, "pages": 240, "year": 2022}
]
collection.insert_many(school_books)
print("Шкільні книги успішно додано.\n")



print("-" * 50)
print("1. Книги для класів з 5 по 8 включно:")
query_classes = {"class_level": {"$gte": 5, "$lte": 8}}
for book in collection.find(query_classes):
    print(f" - {book['title']} ({book['class_level']} клас), сторінок: {book['pages']}")


print("-" * 50)
print("2. Топ-3 книги 2022 року (сортування за спаданням класів):")
query_2022 = {"year": 2022}
results_2022 = collection.find(query_2022).sort("class_level", pymongo.DESCENDING).limit(3)
for book in results_2022:
    class_info = f"{book['class_level']} клас" if "class_level" in book else "Поза програмою"
    print(f" - {book['title']} ({class_info}), Рік: {book['year']}")


print("-" * 50)
print("3. Книга з найбільшою кількістю сторінок:")
biggest_book = collection.find().sort("pages", pymongo.DESCENDING).limit(1)
for book in biggest_book:
    print(f" - {book['title']} ({book['pages']} сторінок)")
print("-" * 50)