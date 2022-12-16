import random


class Human:
    def __init__(self, studies_gladness=None, knowledge=None, name='Human', studies=None, job=None, home=None, car=None):
        self.knowledge = knowledge
        self.studies_gladness = studies_gladness
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50

    def get_learn(self):
        if self.studies():
            pass
        else:
            self.knowledge()
            return
        self.studies = Studies(studies_list)
        self.knowledge += self.studies.knowledge
        self.studies_gladness -= self.studies.studies_gladness

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def get_knowledge(self):
        self.knowledge = Studies(studies_list)

    def get_studies_gladness(self):
        self.studies_gladness = Studies(studies_list)

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_home(self):
        self.home = House()

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 10:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness
        self.satiety -= 5
        self.knowledge += 10

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 10:
                manage = 'fuel'
            else:
                self.to_repair()
                return
        if manage == 'fuel':
            print('I bought fuel')
            self.money -= 50
            self.car.fuel += 100
        elif manage == 'food':
            print('Bought food')
            self.money -= 20
            self.home.food += 20
        elif manage == 'delicacies':
            print('Happy')
            self.money -= 20
            self.satiety += 5
            self.gladness += 2

    def chill(self):
        self.gladness += 10
        self.home.mess += 5
        self.money -= 50
        self.studies.knowledge -= 30
        self.studies_gladness += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
        self.studies_gladness += 3

    def to_repair(self):
        self.car.strength += 100
        self.money -= 100

    def days_indexes(self, day):
        day = f"Today the {day} of {self.name}'s life"
        print(f'{day:=^50}')
        human_indexes = self.name + "'s indexes"
        print(f'{human_indexes:+^50}')
        print(f'Money = {self.money}')
        print(f'Satiety = {self.satiety}')
        print(f'Gladness = {self.gladness}')
        print(f'Studies_Gladness {self.studies_gladness}')
        print(f'Knowledge {self.knowledge}')

        home_indexes = 'Home indexes'
        print(f'{home_indexes:^50}')
        print(f'Food = {self.home.food}')
        print(f'Mess = {self.home.mess}')

        car_indexes = f"{self.car.brand} car indexes"
        print(f'{car_indexes:^50}')
        print(f'Fuel = {self.car.fuel}')
        print(f'Strength = {self.car.strength}')

    def is_alive(self):
        if self.gladness < 0:
            print('Depression...')
            return False
        if self.satiety < 0:
            print('Dead....')
            return False
        if self.money < -500:
            print('Bankrupt...')
            return False
        if self.studies_gladness < 0:
            return False
        if self.knowledge < -10:
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print('Settled in the home')
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, going to get a job {self.job.job}"
                  f"with salary {self.job.salary}")
        if self.studies is None:
            self.get_learn()
            print(
                f"I don't have a educational institution, going to get a educational institution {self.studies.studies} "
                f"with knowledge {self.studies.knowledge}"
                f" and with studies_gladness {self.studies.studies_gladness}")
        self.days_indexes(day)
        if self.satiety < 20:
            print('Time eat')
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 10:
                print('I clean home')
                self.clean_home()
            else:
                print("Time chill")
                self.chill()
        elif self.money < 5:
            print('Time work')
            self.work()
        elif self.car.strength < 10:
            print('I need to repair my car')
            self.to_repair()
        dice = random.randint(1, 5)
        if dice == 1:
            print("Let's go chill")
            self.chill()
        elif dice == 2:
            print('Start working')
            self.work()
        elif dice == 3:
            print('Cleaning time!')
            self.clean_home()
        elif dice == 4:
            print('Time for treats')
            self.shopping(manage='delicacies')
        elif dice == 5:
            print('Time for learning')
            self.get_learn()


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= 10
            self.strength -= 1
            return True
        else:
            print('The car cannot move')
            return False


class House:
    def __init__(self):
        self.food = 0
        self.mess = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness = job_list[self.job]['job_gladness']


class Studies:
    def __init__(self, studies_list):
        self.studies = random.choice(list(studies_list))
        self.knowledge = studies_list[self.studies]['knowledge']
        self.gladness = studies_list[self.studies]['studies_gladness']


studies_list = {'school': {'knowledge': 50, 'studies_gladness': 4},
                'college': {'knowledge': 70, 'studies_gladness': 7},
                'university': {'knowledge': 90, 'studies_gladness': 5}}

job_list = {'C++': {'salary': 90, 'job_gladness': 3},
            'Python': {'salary': 50, 'job_gladness': 10},
            'Java': {'salary': 70, 'job_gladness': 7},
            'PHP': {'salary': 40, 'job_gladness': 5}}

brands_of_car = {"BMW": {'fuel': 100, 'strength': 100, 'consumption': 6},
                 "Lada": {'fuel': 50, 'strength': 30, 'consumption': 9},
                 "Ford": {'fuel': 80, 'strength': 150, 'consumption': 8},
                 "Audi": {'fuel': 70, 'strength': 120, 'consumption': 7}}

nick = Human(name='Nick')
for day in range(1, 8):
    if nick.live(day) == False:
        break
