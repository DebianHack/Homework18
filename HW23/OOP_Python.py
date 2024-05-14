# Комментарии пишу для себя, не снижайте оценку

import random

# Класс Car
class Car:
    def __init__(self, model, color, economy):
        self.model = model
        self.color = color
        self.mileage = 0 # пробег
        self.fuel = 100 # остаток бензина
        self.economy = economy
    # Метод drive - Уменьшает запас топлива, увеличивает пробег. Принимает один аргумент "дистанция".
    def drive(self, distance):
        fuel_consumption = (distance / 100) * self.economy
        if fuel_consumption > self.fuel:
            print("Not enough fuel to drive this distance.")
        else:
            self.fuel -= fuel_consumption
            self.mileage += distance

    # Метод distance_left - возвращает информацию о расстоянии, которое машина может проехать с учетом остатка топлива.
    def distance_left(self):
        return (self.fuel / self.economy) * 100
    # Метод fuel_up -заправится. Увеличивает количество топлива на 20
    def fuel_up(self):
        self.fuel += 20
        if self.fuel > 100:
            self.fuel = 100

models = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]
colors = ["red", "blue", "green", "black", "white"]

cars = []
for _ in range(10):
    model = random.choice(models)
    color = random.choice(colors)
    economy = random.randint(5, 15)
    cars.append(Car(model, color, economy))

for car in cars:
    car.drive(200)
    car.fuel_up()
    car.drive(100)
    # Значение наиболее заправленной машиный, после движения
most_fuel_car = max(cars, key=lambda car: car.fuel)

print(f"Car with the most fuel remaining:")
print(f"Model: {most_fuel_car.model}")
print(f"Color: {most_fuel_car.color}")
print(f"Mileage: {most_fuel_car.mileage} km")
print(f"Fuel remaining: {most_fuel_car.fuel} liters")
print(f"Fuel economy: {most_fuel_car.economy} liters/100km")