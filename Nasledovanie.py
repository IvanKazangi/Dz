# class Human:
#     height = 170
#
#
# class Student(Human):
#     pass
#
#
# class Worker(Human):
#     pass
#
#
# st = Student()
# st.height
# print(st.height)
# wk = Worker()
# print(wk.height)
# st.height = 190
# print(st.height)
# print(wk.height)
# wk.height = 200
# print(wk.height)
# print(Human.height)


# class Human:
#     height = 170
#
#
# class Student(Human):
#     height = 150
#
#
# class Worker(Human):
#     height = 200
#
#
# st = Student()
# st.height
# print(st.height)
# wk = Worker()
# print(wk.height)

# class Grandparent:
#     height = 150
#     satiety = 50
#     age = 75
#
#
# class Parent(Grandparent):
#     age = 40
#
#
# class Child(Parent):
#     height = 100
#
#     def __init__(self):
#         print(self.height)
#         print(self.age)
#         print(self.satiety)
#
# nick = Child()

# class Hello_World:
#     hello = "Hello"
#     _hello = "_Hello"
#     __hello = "__Hello"
#
#     def __init__(self):
#         self.world = "World"
#         self._world = "_World"
#         self.__world = "__World"
#
#     def _printer(self):
#         print(self.hello)
#         print(self._hello)
#         print(self._hello)
#         print(self.__hello)
#         print(self.world)
#         print(self._world)
#         print(self.__world)
#         print(self.__hello)
#         print(self.world)
#         print(self._world)
#         print(self.__world)
#
#     def __printer(self):
#         pass
#
#
# class Hi(Hello_World):
#     def hi_printer(self):
#         print(self.hello)
#         print(self._hello)
#         # print(self.__hello)
#         print(self.world)
#         print(self._world)
#         # print(self.__world)
#
#
# hello = Hello_World()
# hello._printer()
# hi = Hi()
# hi.hi_printer()
# hi.__printer()


# class Class1:
#     var = 20
#
#     def __init__(self):
#         self.var = 10
#
# class Class2(Class1):
#     def __init__(self):
#         print(self.var)
#         super().__init__()
#         print(self.var)
#
# obj = Class2()

# class Grandparent:
#     def about(self):
#         print("i am Grandparent")
#
#     def about_myself(self):
#         print("i am Grandparent")
#

#
#
# class Parent(Grandparent):
#     def __init__(self):
#         super().__init__()
#
#     def about_myself(self):
#         print("i am Parent")
#
#
# class Child(Parent):
#     def __init__(self):
#         super().about_myself()
#
#
# nick = Child()

# class Computer:
#     def __init__(self):
#         super().__init__()
#         self.memory = 128
#
#
# class Display:
#     def __init__(self):
#         super().__init__()
#         self.resolution = "4K"
#
#
# class Phone(Computer, Display):
#     def printer(self):
#         print(self.memory)
#         print(self.resolution)


# phone = Phone()
# phone.printer()

# import random
#
# help(random)
# r = random
# g = Grandparent
# print(r.__name__)
# print(g.__name__)
# print(dir(Grandparent))
# print(dir(list))
# for _ in dir(list):
#     print(_)

lst = []


# print(hasattr(lst, "add"))
# print(getattr(lst, "append", None))
# print(getattr(lst, "add", None))

# print(issubclass(Phone, Display))
# print(issubclass(Display, Phone))
# print(issubclass(Phone, Computer))
#
# print(isinstance(phone, Phone))
# print(isinstance(phone, Grandparent))
# print(isinstance(phone, object))

# def func():
#     pass
#
#
# import inspect
# import random
#
# print(inspect.ismodule(random))
# print(inspect.ismodule(list))
# print(inspect.isclass(Grandparent))
# print(inspect.isfunction(func))
#
# import sys
#
# print(sys.executable)
# print(sys.version)
# print(sys.platform)
# print(sys.argv)
# print(sys.maxsize)
# print(sys.copyright)
# print(sys.modules)
# print(dir(__builtins__))
# for i in dir(__builtins__)
#     print(i)

# print(len(10))
# print(name)
# for i in range(11):
#    print(i)

try:
    print("Start code")
    a = input("Input a")
    c = a / 0
    print(c)
except NameError:
    print("Stop! a - defined")
except TypeError:
    print("Stop! Type a - error")
except ZeroDivisionError:
    c = 0
    print(c)
else:
    print("ELSE")
