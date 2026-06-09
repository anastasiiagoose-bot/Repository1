from pymongo import MongoClient

cluster_link = "ТВІЙ_РЯДОК_ПІДКЛЮЧЕННЯ_З_MONGODB_ATLAS"
client = MongoClient(cluster_link)

db = client["book_database"]      # База даних книг
collection = db["books_collection"]  # Колекція книг

collection.delete_many({})


game_of_thrones = {
    "title": "Гра престолів",
    "price": 450,
    "year": 1996,
    "pages": 800
}
collection.insert_one(game_of_thrones)

school_books = [
    {"title": "Математика", "grade": 5, "pages": 250, "year": 2022},
    {"title": "Історія України", "grade": 7, "pages": 180, "year": 2022},
    {"title": "Біологія", "grade": 8, "pages": 210, "year": 2021},
    {"title": "Географія", "grade": 6, "pages": 195, "year": 2022},
    {"title": "Українська література", "grade": 9, "pages": 320, "year": 2022},
    {"title": "Фізика", "grade": 7, "pages": 150, "year": 2022}
]
collection.insert_many(school_books)

print("--- Дані успішно додані в MongoDB ---\n")


print("1. Книги для 5-8 класів:")
query_grades = {"grade": {"$gte": 5, "$lte": 8}}
for book in collection.find(query_grades):
    print(f"- {book['title']} ({book['grade']} клас)")

print("\n" + "="*40 + "\n")


print("2. Книги 2022 року (сортування від більшого класу, макс 3):")
query_year = {"year": 2022}

for book in collection.find(query_year).sort("grade", -1).limit(3):
    print(f"- {book['title']} | Клас: {book['grade']} | Рік: {book['year']}")

print("\n" + "="*40 + "\n")


print("3. Книга з найбільшою кількістю сторінок:")

biggest_book = collection.find().sort("pages", -1).limit(1)
for book in biggest_book:
    print(f"- {book['title']} ({book['pages']} сторінок)")