import random

a = random.randint(0, 99)
b = random.randint(0, 99)


class Hidden_calculation:

    _calculation = (a - b)

    def Sum_printer(self):
        print(self._calculation)


calculation1 = Hidden_calculation()
calculation1.Sum_printer()
