import requests


url = "https://dummyjson.com/recipes"
response = requests.get(url)
data = response.json()
recipes = data["recipes"]


pizza_recipes = [r["name"] for r in recipes if "Pizza" in r["name"]]


italian_count = 0
for r in recipes:
    if r["cuisine"] == "Italian":
        italian_count += 1


most_caloric_dish = max(recipes, key=lambda x: x["caloriesPerServing"])


temp_190_dishes = []
for r in recipes:
    first_instruction = r["instructions"][0]
    if "190" in first_instruction:
        temp_190_dishes.append(r["name"])


total_reviews = sum(r["reviewCount"] for r in recipes)

print(f" Рецепти піци: {pizza_recipes}")
print(f"🇮🇹 Кількість італійських страв: {italian_count}")
print(f" Найкалорійніша страва: {most_caloric_dish['name']} ({most_caloric_dish['caloriesPerServing']} kcal)")
print(f" Готуються при 190°C: {temp_190_dishes}")
print(f" Загальна кількість переглядів: {total_reviews}")