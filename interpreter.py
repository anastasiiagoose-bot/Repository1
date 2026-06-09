
def check_integer(func):
    def wrapper():

        result = func()


        if type(result) == int:
            return result + 10
        else:
            return result

    return wrapper



@check_integer
def get_number_five():
    return 5



@check_integer
def get_number_point_five():
    return 5.5


# Перевірка роботи
print(get_number_five())
print(get_number_point_five())