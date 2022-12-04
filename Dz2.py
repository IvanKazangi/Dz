import random


class Auto:
    def __init__(self,  brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def to_fuel(self):
        print("Time to fill the car...")
        self.fuel == self.brand

    def to_strength(self):
        print("Time to repair the car...")
        self.strength == self.brand

    def to_drive(self):
        if self.to_fuel <= self.consumption:
            print("Can not move...")
            self.to_fuel

        elif self.to_fuel >= self.consumption:
            print("Can move...")
            self.fuel -= self.comsumption

        if self.to_strength <= self.strength:
            print("Can not move...")
            self.to_strength

        elif self.to_strength >= self.strength:
            print("Can move...")
            self.strength -= 1


brands_of_car = {"BMW": {"fuel": 100, "strength": 100, "consumption": 6},
                 "Lada": {"fuel": 50, "strength": 30, "consumption": 9},
                 "Ford": {"fuel": 80, "strength": 150, "consumption": 8},
                 "Audi": {"fuel": 70, "strength": 120, "consumption": 7}}
brand_list = (list(brands_of_car.keys()))
print(brand_list[0])
print(brands_of_car[brand_list[0]])
