"""
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал". Done
Створіть об'єкт цього класу, представляючи студента. Done
Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента. Done
Виведіть інформацію про студента та змініть його середній бал. Done
"""

class Student:
    def __init__(self, name, surname, age, average_score):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_score = average_score

    def change_score(self, new_score):
        self.average_score = new_score

student_alex = Student(name="Олександр", surname="Абраменко", age=26, average_score=80)
print(f"Це студент, {student_alex.name} {student_alex.surname}, йому {student_alex.age} "
      f"та його середній бал складає: {student_alex.average_score}")
student_alex.change_score(85)
print(f"Новий середній бал складає: {student_alex.average_score}")



