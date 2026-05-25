from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, fuel: float, health: int = 100):
        self.fuel = fuel
        self.health = health

    @property
    def is_working(self) -> bool:
        return self.health > 20

    def move(self, distance: float):
        if not self.is_working:
            print("Рух неможливий: транспорт потребує ремонту!")
            return

        fuel_needed = distance * 0.1
        if self.fuel < fuel_needed:
            print("Рух неможливий: недостатньо пального!")
            return

        self.fuel -= fuel_needed
        self.health -= int(distance * 0.05)
        print(f"Пройдено {distance} км. Пальне: {self.fuel}, Стан: {self.health}")

    @abstractmethod
    def __str__(self) -> str:
        pass


class Car(Transport):
    def __init__(self, model: str):
        super().__init__(fuel=50)
        self.model = model

    def __str__(self) -> str:
        return f"Автомобіль {self.model} (Пальне: {self.fuel}, Стан: {self.health})"


class Truck(Transport):
    def __init__(self, name: str):
        super().__init__(fuel=120)
        self.name = name

    def __str__(self) -> str:
        return f"Вантажівка {self.name} (Пальне: {self.fuel}, Стан: {self.health})"


class Motorcycle(Transport):
    def __init__(self, brand: str):
        super().__init__(fuel=20)
        self.brand = brand

    def __str__(self) -> str:
        return f"Мотоцикл {self.brand} (Пальне: {self.fuel}, Стан: {self.health})"


class ServiceStation:
    def repair(self, transport_unit: Transport):
        transport_unit.health = 100
        print(f"Транспорт відремонтовано! Поточний стан: {transport_unit.health}")


# Перевірка
if __name__ == "__main__":
    car = Car("Toyota")
    truck = Truck("Volvo")
    moto = Motorcycle("Yamaha")
    station = ServiceStation()

    print("--- Перевірка виведення __str__ та __dict__ ---")
    print(car)
    print(car.__dict__)

    print("\n--- Перевірка руху та властивості is_working ---")
    print(f"Чи справна машина? {car.is_working}")
    car.move(150)

    print("\n--- Перевірка відсутності пального ---")
    moto.move(300)

    print("\n--- Перевірка поганого технічного стану ---")
    truck.condition = 10
    print(f"Чи справна вантажівка? {truck.is_working}")
    truck.move(10)

    print("\n--- Перевірка ремонту (СТО) ---")
    print("Ремонт зламаного:")
    station.repair(truck)
    truck.move(50)

    print("\nРемонт робочого та кілька ремонтів поспіль:")
    station.repair(car)
    station.repair(car)