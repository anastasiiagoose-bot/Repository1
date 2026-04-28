
def average(a, b, c):
    result = (a + b + c) / 3
    return round(result, 2)


def foo_check(something) -> bool:
    return something > 10 and something % 2 == 0


def count_vowels(text: str) -> int:
    vowels = "aeiouyAEIOUY"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


if __name__ == "__main__":
    print(f"Середнє значення: {average(5, 7, 9)}")
    print(f"Число 12 парне і > 10: {foo_check(12)}")
    print(f"Число 8 парне і > 10: {foo_check(8)}")
    print(f"Кількість голосних в 'Hello Python': {count_vowels('Hello Python')}")