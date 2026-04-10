car_data = {
    "model": "Toyota RAV4 Hybrid",
    "price": 1650000,
    "engine_volume": "2487 cm3",
    "gross_weight": 2225,
    "max_speed": 180,
    "fuel_consumption": 4.8,
    "interior_features": [
        "Multimedia 10.5",
        "Digital panel 12.3",
        "Leather seats",
        "Climate control"
    ],
    "trunk_params": {
        "standard_volume": 580,
        "folded_seats_volume": 1690
    }
}

car_data["max_trailer_weight_with_brakes"] = 800


print(f"--- Інформація про автомобіль ---")
print(f"Назва авто: {car_data['model']}")
print(f"Ціна: {car_data['price']} грн")


print(f"Перша опція інтер'єру: {car_data['interior_features'][0]}")


folded_vol = car_data['trunk_params']['folded_seats_volume']
print(f"Об'єм багажника (складені сидіння): {folded_vol} л")


insurance_fee = car_data['price'] * 0.005
car_data["insurance_fee"] = insurance_fee
print(f"Страховий платіж (0.5%): {insurance_fee} грн")


distance = 200
fuel_price = 93
trip_cost = (car_data['fuel_consumption'] / 100) * distance * fuel_price

print(f"\n--- Розрахунок мандрівки ---")
print(f"Вартість поїздки на {distance} км при ціні {fuel_price} грн/л: {trip_cost:.2f} грн")


print("\nОновлені дані про авто:", car_data)