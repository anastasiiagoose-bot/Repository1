from functions import calculate, format_text, sum_string_numbers

#1
print(calculate(10, 5, "sub"))
print(calculate(a=20, b=10, operation="sum"))
data_calc = {"a": 50, "b": 20, "operation": "sub"}
print(calculate(**data_calc))

#2
print(format_text("Hello World", False))
print(format_text(text="python", upper=True))
data_text = {"text": "PyCharm", "upper": False}
print(format_text(**data_text))

#3
print(sum_string_numbers("10;20;30", ";"))
print(sum_string_numbers(numbers_str="5,10,15", separator=","))
data_sum = {"numbers_str": "1,2,3,4,5", "separator": ","}
print(sum_string_numbers(**data_sum))