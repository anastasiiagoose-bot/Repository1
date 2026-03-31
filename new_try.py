apples = "3"
pears = "2"
# print(type(apples))

apples = int(apples)
# print(type(apples))

integer_number = 1_000
integer_number2 = 10_001
summa = integer_number + integer_number2
print(summa)
print("Сума:", summa, 'in total')
print(f"{summa=}")
print(f"{2+2=}")

pears = int(pears)

total_fruits = apples + pears
# total_fruits_cost = total_fruits * "156"

print(f"{total_fruits=}")

n1 = 12
n2 = 244
diffrence = n1 - n2
print(f"{diffrence=}")

n3 = -300
n4 = -200
mult = n1 * n2
print(f"{mult=}")

n5 = 20
n6 = 5
fraction = n5 / n6
print(f"{fraction=}")

not_integer = 5.0
not_integer2 = 5.0
not_number2 = 1_001
not_integer_summa = not_integer + not_integer2 + not_number2
print(f"{not_integer_summa=}")


bananas_quantity = input('Enter the number of bananas: ')
bananas_quantity = float(bananas_quantity)
banana_cost_per_unit = 100
total_bananas_cost = bananas_quantity * banana_cost_per_unit
print(f"{total_bananas_cost=}")

rounded_total_banana_cost = round(total_bananas_cost)
print(f"{rounded_total_banana_cost=}")

