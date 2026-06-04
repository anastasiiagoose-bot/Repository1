phone = {'title': 'iPhone 17', "price": 65000, 'description': "cool"}
created_phone = collection_phones.insert_one(phone)
print(created_phone)

# add many
phones = [
    {'title': 'iPhone 17', "price": 65000, 'description': "cool"},
    {'title': 'iPhone 16', "price": 65000, 'description': "cool"},
    {'title': 'iPhone 15', "price": 65000, 'description': "cool"},
    {'title': 'iPhone 14', "price": 65000, 'description': "cool", 'is_restored': True},
]
created_phones = collection_phones.insert_many(phones)
print(created_phones)