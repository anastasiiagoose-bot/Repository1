
numbers = [1, 5, 2, 8, 3, 7]


max_num = max(numbers)
min_num = min(numbers)
total_sum = sum(numbers)


print("--- Завдання 1 ---")
print(f"Список чисел: {numbers}")
print(f"Найбільше число: {max_num}")
print(f"Найменше число: {min_num}")
print(f"Сума всіх чисел: {total_sum}")


grades = [10, 8, 12, 7, 9]


average = sum(grades) / len(grades)


print("\n--- Завдання 2 ---")
print(f"Оцінки: {grades}")
print(f"Середній бал: {average}")


print("Оцінки вище середнього:")
for grade in grades:
    if grade > average:
        print(grade)
