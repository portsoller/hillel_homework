"""
Завдання 1
Створіть клас Employee, який має атрибути name та salary. +
Далі створіть два класи, Manager та Developer, які успадковуються від Employee. +
Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language. +
Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer. +
Цей клас представляє керівника з команди розробників.
Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ),
а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник. +
Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead +
"""

class Employee:
    def __init__(self, name, salary):
            self.name = name
            self.salary = salary

class Manager(Employee):
    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)
        self.department = department

class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        super().__init__(**kwargs)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        super().__init__(name=name, salary=salary, department=department, programming_language=programming_language)
        self.team_size = team_size

    def __str__(self):
        return (f"My name is {self.name}. My salary is {self.salary} and I worked as a {self.department}. "
                f"My teamsize {self.team_size} people and our programming language is {self.programming_language}")

team_lead = TeamLead("Peter", 20000, department="Manager", team_size=3, programming_language="Python")
print(team_lead)
print(team_lead.__dict__)

"""
Завдання 2
Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру. +
Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.+ 
Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор. +
Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.
"""
from abc import ABC, abstractmethod

class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def area(self):
        return self.__side_a * self.__side_b

    def perimeter(self):
        return (self.__side_a + self.__side_b) * 2

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return 3.14 * self.__radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.__radius

class Square(Figure):
    def __init__(self, side_a):
        self.__side_a = side_a

    def area(self):
        return self.__side_a ** 2

    def perimeter(self):
        return self.__side_a * 4

rectangle = Rectangle(side_a=10.9, side_b=20.4)
circle = Circle(radius=10.7)
square = Square(side_a=11.3)

figures = [rectangle, circle, square]
for figure in figures:
    print(f"Фігура: {figure.__class__.__name__}")
    print(f"Площа фігури: {round(figure.area(), 2)}")
    print(f"Периметр фігури: {round(figure.perimeter(), 2)}")
    print("----------------------------------------")