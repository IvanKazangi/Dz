# class Human:
#     def __init__(self, name):
#         self.name = name
#
# class Auto:
#     def __init__(self,brand):
#         self.brand = brand
#         self.passengers = []
#     def add_passengers(self, human):
#         self.passergers.append(human)
#
#     def print_passengers(self):
#         if self.passengers != []:
#             print(f"Names of {self.brand} passrengers:")
#             for passengers in self.passengers:
#                 print(passenger)
#
# nick = Human('Nick')
# anna = Human("Anna")
# car = Auto("BMW")
# car.add_passengers(nick)
# car.add_passengers(anna)
# car.print_passengers()
import random
class Human:
    def __init__(self, name="Human", job=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satierly = 50

    def get_job(self):
        pass

    def get_car(self):
        pass

    def get_home(self):
        pass

    def eat(self):
        pass

    def work(self):
        pass

    def shopping(self):
        pass

    def chill(self):
        pass

    def clean_home(self):
        pass

    def to_repair(self):
        pass

    def days_indexes(self):
        pass

    def is_alive(self):
        pass

    def live(self, day):
        pass


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if

class House:
    def __init__(self):


brands_of_car = {"BMW": {"fuel": 100, "strength": 100, "consumption": 6},
                 "Lada": {"fuel": 50, "strength": 30, "consumption": 9},
                 "Ford": {"fuel": 80, "strength": 150, "consumption": 8},
                 "Audi": {"fuel": 70, "strength": 120, "consumption": 7}}
brand_list = (list(brands_of_car.keys()))
print(brand_list[0])
print (brands_of_car[brand_list[0]])