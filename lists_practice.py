
numbers = [3, 7, 2, 9, 4, 6, 1, 8]


even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

doubled_even = []
for num in even_numbers:
    doubled_even.append(num * 2)

if 8 in doubled_even:
    doubled_even.remove(8)


print("Завдання 1 (doubled_even):", doubled_even)


words = ["apple", "banana", "kiwi", "pear", "banana", "plum"]


unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)


long_words = []
for word in unique_words:
    if len(word) > 4:
        long_words.append(word)


upper_words = []
for word in long_words:
    upper_words.append(word.upper())


if "BANANA" in upper_words:
    print("Слово BANANA знайдено у списку!")


print("Завдання 2 (upper_words):", upper_words)