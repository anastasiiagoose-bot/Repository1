class Car:
    def __init__(self, model: str, age: int, owner: str = "Немає", fuel: float = 0):
        self.model = model
        self.age = age
        self.owner = owner
        self.fuel = fuel
        self.car_id = id(self)

    def __str__(self) -> str:
        return f"{self.model}, {self.age}р., {self.owner}, {self.fuel}л"

    def refuel(self, amount: float):
        self.fuel += amount

    @property
    def status_by_age(self) -> str:
        if self.age <= 3:
            return "нове авто"
        elif self.age <= 10:
            return "середній стан"
        return "старе авто"

    @property
    def fuel_status(self) -> str:
        return "Потрібно заправитись" if self.fuel < 10 else "Можна їхати далеко"


if __name__ == "__main__":
    # Створення обєктів

    car1 = Car("Toyota", 2, "Олег", 5)
    car2 = Car("BMW", 12, fuel=15)

    # Перевірки

    print(car1.car_id, car2.car_id)
    print(car1.__dict__)
    print(car2.__dict__)
    print(car1)
    print(car2)

    # Зміна бензину

    car1.fuel = 8
    car2.refuel(20)

    # Перевірка властивостей
    print(car1.status_by_age, car1.fuel_status)
    print(car2.status_by_age, car2.fuel_status)

    # Порівняння пального
    if car1.fuel > car2.fuel:
        print(f"В {car1.model} більше пального")
    else:
        print(f"В {car2.model} більше пального")