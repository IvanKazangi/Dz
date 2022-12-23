class Table:
    def __init__(self):
        super().__init__()
        self.material = "wood"
        self.fixed_clasps = "nails"


class Armchair:
    def __init__(self):
        super().__init__()
        self.material1 = "cloth"
        self.subject_of_support = "springs"


class Bed(Armchair, Table):
    def printer(self):
        print(self.material)
        print(self.fixed_clasps)
        print(self.subject_of_support)
        print(self.material1)

bed = Bed()
bed.printer()