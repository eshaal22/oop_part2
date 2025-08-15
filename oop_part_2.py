# ---------- Delete attribute example ----------
# class Student:
#     def __init__(self, name):
#         self.name = name
#
# s1 = Student("eshaal")
# print(s1.name)
# del s1.name
# print(s1.name)  # error: deleted attribute

# ---------- Private attribute example ----------
# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass
#
#     def reset_pass(self):
#         print(self.__acc_pass)
#
# acc1 = Account("12345", "abcde")
# print(acc1.acc_no)
# print(acc1.reset_pass())

# ---------- Private method example ----------
# class Person:
#     __name = "eshaal"
#     def __hello(self):
#         print("hello user!")
#     def welcome(self):
#         self.__hello()
#
# p1 = Person()
# print(p1.welcome())

# ---------- Single inheritance ----------
# class Car:
#     colour = "black"
#     @staticmethod
#     def start():
#         print("car chalo hogai...")
#     @staticmethod
#     def stop():
#         print("car rukk jao...")
#
# class Toyota(Car):
#     def __init__(self, name):
#         self.name = name
#
# car1 = Toyota("mercedes")
# car1.start()
# print(car1.colour)

# ---------- Multi-level inheritance ----------
# class Car:
#     colour = "black"
#     @staticmethod
#     def start():
#         print("car chalo hogai...")
#     @staticmethod
#     def stop():
#         print("car rukk jao...")
#
# class Toyota(Car):
#     def __init__(self, brand):
#         self.brand = brand
#
# class Fortuner(Toyota):
#     def __init__(self, type):
#         self.type = type
#
# car1 = Fortuner("diesel")
# car1.start()

# ---------- Multiple inheritance ----------
# class A:
#     varA = "welcome to class a"
# class B:
#     varB = "welcome to class b"
# class C(A, B):
#     varC = "welcome to the c"
# c1 = C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

# ---------- Super method ----------
# class Car:
#     def __init__(self, type):
#         self.type = type
#     @staticmethod
#     def start():
#         print("car chalo hogai...")
#     @staticmethod
#     def stop():
#         print("car rukk jao...")
#
# class Toyota(Car):
#     def __init__(self, name, type):
#         self.name = name
#         super().__init__(type)
#         super().start()
#
# car1 = Toyota("civic", "electric")
# print(car1.type)
# print(car1.name)

# ---------- Class method ----------
# class Person:
#     name = "anonymous"
#     @classmethod
#     def changename(cls, name):
#         cls.name = name
#
# p1 = Person()
# p1.changename("eshaal atif")
# print(p1.name)
# print(Person.name)

# ---------- Property decorator ----------
# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math) / 3) + "%"
#
# stu1 = Student(98, 97, 99)
# print(stu1.percentage)
# stu1.phy = 86
# print(stu1.percentage)

# ---------- Polymorphism ----------
# print(1 + 2)
# print("apna" + "college")
# print([1, 2, 3] + [4, 5])

# ---------- Operator overloading ----------
# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img
#     def showNumber(self):
#         print(self.real, "i +", self.img, "j")
#     def __sub__(self, num2):
#         newReal = self.real - num2.real
#         newImg = self.img - num2.img
#         return Complex(newReal, newImg)
#
# num1 = Complex(1, 3)
# num1.showNumber()
# num2 = Complex(4, 3)
# num2.showNumber()
# num3 = num1 - num2
# num3.showNumber()

# ---------- Practice Q1: Circle ----------
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return (22 / 7) * self.radius ** 2
#     def perimeter(self):
#         return 2 * (22 / 7) * self.radius
#
# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())

# ---------- Practice Q2: Employee ----------
# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary
#     def showdetails(self):
#         print("role =", self.role)
#         print("dept =", self.dept)
#         print("sal =", self.salary)
#
# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__(
