from pprint import pprint

login = 'admin'
password = '123'
another_key = "key"

list_ = []
number = 66.9
test_dict = {'data': 123}

admin_data = {
    "login": "admin",
    "password": password,
    # another_key: another_key,
    "name": "Андрій",
    "hobbies": ['soccer', 'darts'],
    "age": 49,
    "address": {
        "city": "Одеса",
        'street': "Перша",
        'house': None
    },
    "is_married": True,
    "salary_usd": 3_000,
}

# print(type(number))

# get data

admin_age = admin_data['age']
print(admin_age)

pprint(admin_data, indent=4, width=40)

admin_wife_name = admin_data.get("wife_name")
print(admin_wife_name)

admin_salary_uds = admin_data.get("salary_usd", 1000)  # None => False
print(admin_salary_uds)
grn_to_usd_rate = 43.72
admin_salary_grn = round(admin_salary_uds * grn_to_usd_rate, 2)
print(admin_salary_grn)



admin_hobbies = admin_data.get('hobbies', [])
has_admin_hobbies = bool(admin_hobbies)
has_admin_hobbies = len(admin_hobbies) >= 1

if admin_hobbies:
    print(admin_hobbies)
    first_hobby = admin_hobbies[0]
    print(first_hobby)

    admin_address = admin_data.get('address', {})
    admin_city = admin_address.get('city', "No data")
    print(admin_city)

# update
# add data
admin_data['favorite_candy'] = 'Korivka'
pprint(admin_data, indent=4)

# change data
admin_data['age'] = 39
pprint(admin_data, indent=4)

admin_data['address']['street'] = 'Садова'
admin_data['hobbies'].append('tennis')
pprint(admin_data, indent=4)

extra_admin_data = {
    'pet': "dog",
    'address': None
}
# create new dict merged
# full_admin_data = admin_data | extra_admin_data
full_admin_data = {**admin_data, **extra_admin_data}
pprint(full_admin_data, indent=4)

# update existing
admin_data.update(**extra_admin_data)
pprint(admin_data, indent=4)

#
# delete
# del admin_data["address"]
address = admin_data.pop("address")
print(address)
pprint(admin_data, indent=4)