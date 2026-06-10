"""
Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:

сторона_а (довжина сторони a). Done
кут_а (кут між сторонами a і b). Done
кут_б (суміжний з кутом кут_а).
Необхідно реалізувати наступні вимоги:

Значення сторони сторона_а повинно бути більше 0. Done
Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180 Done
Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
Для встановлення значень атрибутів використовуйте метод __setattr__.
"""
class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == 'side_a':
            if value <= 0:
                raise ValueError("Сторона має бути більша за нуль")

            super().__setattr__(name, value)

        elif name == "angle_a":
            if value <= 0 or value >= 180:
                raise ValueError("Кут має бути між 0 та 180 градусами")
            super().__setattr__(name, value)
            super().__setattr__('angle_b', 180 - value)

        else:
            super().__setattr__(name, value)

    def __str__(self):
        return f"Ромб. Сторона: {self.side_a}, кут А: {self.angle_a} та кут В: {self.angle_b}"


rhombus = Rhombus(25, 110)
print(rhombus)
# rhombus2 = Rhombus(0, 95)
# print(rhombus2)
# rhombus3 = Rhombus(15, 181)
# print(rhombus3)