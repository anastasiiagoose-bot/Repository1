
import messages

# Ім'я
name_input = input(messages.MSG_INPUT_NAME).strip()

if name_input.isalpha():
    formatted_name = name_input.title()
    print(messages.MSG_NAME_OK.format(name = formatted_name))
else:
    print(messages.MSG_NAME_ERROR)

# Вік
age_input = input(messages.MSG_INPUT_AGE).strip().lstrip('0')

if age_input.isdigit():
    print(messages.MSG_AGE_OK.format(age = age_input))
else:
    print(messages.MSG_AGE_ERROR)

# Номер телефону
phone_input = input(messages.MSG_INPUT_PHONE).strip()

if phone_input.isdigit():
    print(messages.MSG_PHONE_OK.format(phone = phone_input))
else:
    print(messages.MSG_PHONE_ERROR)

#Фініш
print(messages.MSG_FINISH)





