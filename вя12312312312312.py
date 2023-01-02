class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            number = self.current
            self.current += 1
            return number
        raise StopIteration

for i in MyRange(1, 10):
    print(i, end=" ")
print()
for i in range(1, 10):
    print(i, end=" ")

def count_up_to(x):
    count = 1
    while count <= x:
        yield count ** 2
        count += 1
count = count_up_to(1500000)
n = int(input("N "))
for i in range(1500000):
    print(count.__next__())

lst = []
for i in range(1, 1500000):
    lst.append(i ** 2)
print(lst)

p = print
p(10 + 15)
p("Hello world")


def func():
    age = 15
    print(age)


f = func
f()
print(age)

def first(value):
    name = value