# input()
from pywebio.output import put_markdown, put_text, put_image

import pictures
import prices


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

put_image(pictures.PICTURE_CAVIAR)
put_text(f"Caviar (10g) for {prices.PRICE_CAVIAR_10g} grivnas")

put_image(pictures.PICTURE_DESSERT)
put_text(f"Desert for {prices.PRICE_DESSERT} grivnas")

put_markdown("## Additional:" )

put_text(f"Sause for {prices.PRICE_SAUCE} grivnas")

put_text(f"Cheese for {prices.PRICE_CHEESE} grivnas")

put_text(f"Herbs for {prices.PRICE_HERBS} grivnas")

put_markdown("## Drinks:" )

put_text(f"Cola for {prices.PRICE_COLA_05l} grivnas")

