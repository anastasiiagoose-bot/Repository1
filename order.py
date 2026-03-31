#import
from letter import LETTER_TEMPLATE

#constants
client_name = input("Введіть ім'я та прізвище: ")
travel_date = input("Введіть дату поїздки (наприклад, 15.06.2024): ")
persons_count = int(input("Введіть кількість осіб: "))

#price per person
PRICE_PER_PERSON = 15000
total_price = persons_count * PRICE_PER_PERSON


#procents
if persons_count > 5:
    discount_amount = total_price * 0.05
else:
    discount_amount = 0

final_price = total_price - discount_amount



#result
result_letter = LETTER_TEMPLATE.format(
    name=client_name,
    date=travel_date,
    persons=persons_count,
    price_per_person=PRICE_PER_PERSON,
    total_price=total_price,
    discount=discount_amount,
    final_price=final_price
)

print(result_letter)