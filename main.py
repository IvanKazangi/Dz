# class Student:
#     def __init__(self, height=150):
#         self.age = 18
#         self.height = height
#
#     def printer_age(self):
#         return self.age
#
#     def grow(self, new_height=1):
#         self.height += new_height
#
# st1 = Student ()
# print (st1.age)
# print(st1.printer_age())
# st1.grow(new_height=10)
# print(st1.height)

# class Student:
#      def __init__(self, name=None, height=150):
#          self.height = height
#          self.name = name
#          self.a = a
#          self.b = b
#
#     def __str__(self):
#         return f"i am a student. My name is {self.name}"
#         print("STR")
#
#     def __del__(self):
#         print("DELETE")
#
#     def __bool__(self):
#         return self.name != None
#
#     def __len__(self):
#         return self.height
#
#     def __add__(self, a, b):
#         return self.a - self.b
#
# st1 = Student ()
# print(st1.__bool__())
# print(st2.__bool__())
# st2 = Student("Anna")
# print(st1.__len__())
# print(st2.__len__())
# st = Student()
# a=2
# b=5
# print(st.__add__(a, b))
# print(2+8)
