my_hobbies = (
    "soccer tennis chess   ,      kdghku e guegyery guoe"
    "rh guieriugi yergreg yertuygoiuerygiouryiougyrte"
    "iouygiu  rtgyrtiougyrtyirtyrtitrryiourtitrgti ut"
)
# print(my_hobbies)
name = 'Alex'
name2 = 'Bob'
print(name)
something_new = my_hobbies.split()
# print(something_new)
my_list0a = []
my_list0b = ['apples', 'milk', 'bread']
my_list1 = ['soccer', 'tennis', 'chess']
# print("#")


my_products = [
    'apples',  # macintosh
    'milk',
    'bread',
    'milk',  # selyanske
    'bread',
    'milk',
    'bread',
    'milk',
    'bread',
    'bread',
    'bread',
    'milk',
    # "#' ,      ",
    # "data",
    # "amazon",
]
print(my_products)

# for product in my_products:
#     print(product)

people = [
    "Гордей",
    "Олександр чикота",
    "анастасія Дворник",
    "Вадим ЧернЯков",
    "Іван Яблонський",
]

MSG_WELCOME = 'Привіт, шановний учасник {name}!'

for person in people:
    normalized_person = person.title()
    msg = MSG_WELCOME.format(name=normalized_person)
    print(msg)

# print(33333333)
print(people)
# print(person)   forbidden


money = [
    33,
    1110.50,
    676,
    100,
]

total_income = 0
for income_suma in money:
    total_income = total_income + income_suma
    print(total_income)

print(total_income)

string = 'dgvhjdfvhkdfhvdfhkvhdfhvjdf fk hgh fjgh fj3'
length_of_string = len(string)
print(length_of_string)

length_of_list_money = len(money)
print(length_of_list_money)



