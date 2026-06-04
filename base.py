databases = client.list_databases()
print(databases)
for db in databases:
    print(db)

db_shop = client.shop

collection_books = db_shop.books
collection_phones = db_shop['phones']

# CREATE
# add one document
book = {'title': '10 negro', "price": 365, 'description': "English classic detective"}
collection_books.insert_one(book)