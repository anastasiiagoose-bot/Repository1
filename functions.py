def calculate(a: int = 0, b: int = 0, operation: str = "sum") -> int:
    if operation == "sub":
        return a - b
    return a + b

def format_text(text: str = "", upper: bool = True) -> str:
    if upper:
        return text.upper()
    return text.lower()

def sum_string_numbers(numbers_str: str = "0", separator: str = ",") -> int:
    numbers = numbers_str.split(separator)
    return sum(int(num) for num in numbers)