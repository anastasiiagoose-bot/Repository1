import requests


response = requests.get("http://127.0.0.1:8000/api/animals")
animals = response.json()

venomous_cost = 0
african_count = 0


for animal in animals:

    if animal["is_venomous"] == "так":
        venomous_cost += animal["care_cost"] * animal["count"]


    if animal["continent"] == "Африка":
        african_count += animal["count"]


print(f"Вартість догляду за отруйними: {venomous_cost} грн.")
print(f"Кількість африканських тварин: {african_count} шт.")