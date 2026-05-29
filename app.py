from fastapi import FastAPI

app = FastAPI()


zoo_data = [
    {"species": "Тигр", "care_cost": 5000, "count": 3, "continent": "Азія", "is_venomous": "ні"},
    {"species": "Слон", "care_cost": 8000, "count": 2, "continent": "Африка", "is_venomous": "ні"},
    {"species": "Кобра", "care_cost": 1200, "count": 5, "continent": "Азія", "is_venomous": "так"},
    {"species": "Скорпіон", "care_cost": 300, "count": 10, "continent": "Африка", "is_venomous": "так"},
    {"species": "Удав", "care_cost": 1500, "count": 2, "continent": "Африка", "is_venomous": "ні"}
]


@app.get("/api/animals")
def get_animals():
    return zoo_data