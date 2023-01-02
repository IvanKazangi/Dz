class grade:
    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.current = min

    def __iter__(self):

        return self

    def __next__(self):
        if self.current < self.current:
            number = self.current
            self.current += 1
            return number
        raise StopIteration

for i in grade(1, 12):
    print(i, end=" ")
print()
for i in range(1, 12):
    print(i, end=" ")