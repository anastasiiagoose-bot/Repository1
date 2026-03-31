# input()
from pywebio.input import input, slider
from pywebio.output import put_markdown, put_text, put_image

import pictures
import prices
from discount import DISCOUNT_TRIGGER_COST, DISCOUNT_PERCENTAGE

#Header
put_markdown("# Ресторан \"Смачна Їжа\"")
put_markdown("---")

#Menu
put_markdown("## Menu:" )
put_image(pictures.PICTURE_PIZZA)
put_text(f"Pizza for {prices.PRICE_PIZZA} grivnas")

put_image(pictures.PICTURE_BURGER)
put_text(f"Burger for {prices.PRICE_BURGER} grivnas")

put_image(pictures.PICTURE_STEAK)
put_text(f"Steak (100g) for {prices.PRICE_STEAK_100g} grivnas")

put_image(pictures.PICTURE_CAVIAR, width="300")
put_text(f"Caviar (10g) for {prices.PRICE_CAVIAR_10g} grivnas")

put_image(pictures.PICTURE_DESSERT)
put_text(f"Desert for {prices.PRICE_DESSERT} grivnas")

put_markdown("## Additional:" )

put_text(f"Sause for {prices.PRICE_SAUCE} grivnas")

put_text(f"Cheese for {prices.PRICE_CHEESE} grivnas")

put_text(f"Herbs for {prices.PRICE_HERBS} grivnas")

put_markdown("## Drinks:" )

put_text(f"Cola for {prices.PRICE_COLA_05l} grivnas")




# Order placing
put_markdown("## Ordering:")

quantity_pizza = input("How many pizza do you like?", type="number", min=0, value=1)
quantity_caviar_g = slider(label="How much caviar do you like?", min_value=0, max_value=1000, value=10, step=10)
quantity_caviar = quantity_caviar_g / 10

# calculation
cost_pizza = quantity_pizza * prices.PRICE_PIZZA
cost_caviar = quantity_caviar * prices.PRICE_CAVIAR_10g
total_cost = cost_caviar + cost_pizza

discount_summa = 0
if total_cost >= DISCOUNT_TRIGGER_COST:
    discount_summa = round(total_cost * DISCOUNT_PERCENTAGE / 100, 0)

final_cost = total_cost - discount_summa

# ORDER
put_markdown("## RESULT:")

if cost_pizza:
    put_text(f"🍕Pizza: {quantity_pizza} / {prices.PRICE_PIZZA} grn = {cost_pizza}")
if cost_caviar:
    put_text(f"🍕cost_caviar: {quantity_caviar_g} / {prices.PRICE_CAVIAR_10g} grn/10g = {cost_caviar}")

if total_cost:
    put_text(f"Total cost: {total_cost}")


if discount_summa:
    put_text(f"discount_summa : {discount_summa}")
    put_text(f"))))))))))))))")


put_text(f"final_cost: {final_cost}")
import poems
import sign

AUTHOR_OF_WORK = "Дворник Анаастасія Олександрівна"
student_name = "Dvornyk Anastasiia Oleksandrivna"

print(AUTHOR_OF_WORK.format(student_name))

my_expectations = "Get education and learn python."
print(my_expectations)

symbols = "**************************************************************************"
print(symbols)

POEM_1 = """""
Як умру, то поховайте

Мене на могилі

Серед степу широкого

На Вкраїні милій,

Щоб лани широкополі,

І Дніпро, і кручі

Було видно, було чути,

Як реве ревучий.

Як понесе з України

У синєє море

Кров ворожу... отойді я

І лани і гори —

Все покину, і полину

До самого Бога

Молитися... а до того

Я не знаю Бога.

Поховайте та вставайте,

Кайдани порвіте

І вражою злою кров’ю

Волю окропіте.

І мене в сем’ї великій,

В сем’ї вольній, новій,

Не забудьте пом’янути

Незлим тихим словом.
"""

print(POEM_1)

print(symbols)

POEM_2 = """""
Мені тринадцятий минало.

Я пас ягнята за селом.

Чи то так сонечко сіяло,

Чи так мені чого було?

Мені так любо, любо стало,

Неначе в Бога......

Уже прокликали до паю,

А я собі у бур’яні

Молюся Богу... І не знаю,

Чого маленькому мені

Тойді так приязно молилось,

Чого так весело було.

Господнє небо, і село,

Ягня, здається, веселилось!

І сонце гріло, не пекло!

Та недовго сонце гріло,

Недовго молилось...

Запекло, почервоніло

І рай запалило.

Мов прокинувся, дивлюся:

Село почорніло,

Боже небо голубеє

І те помарніло.

Поглянув я на ягнята —

Не мої ягнята!

Обернувся я на хати —

Нема в мене хати!

Не дав мені Бог нічого!..

І хлинули сльози,

Тяжкі сльози!.. А дівчина

При самій дорозі

Недалеко коло мене

Плоскінь вибирала,

Та й почула, що я плачу. /37/

Прийшла, привітала,

Утирала мої сльози

І поцілувала...

Неначе сонце засіяло,

Неначе все на світі стало

Моє... лани, гаї, сади!..

І ми, жартуючи, погнали

Чужі ягнята до води.



Бридня!.. А й досі, як згадаю,

То серце плаче та болить,

Чому Господь не дав дожить

Малого віку у тім раю.

Умер би, орючи на ниві,

Нічого б на світі не знав.

Не був би в світі юродивим.

Людей і [Бога] не прокляв!
"""

print(POEM_2)

print(symbols)


