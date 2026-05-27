"""Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть код, який сформує новий list (наприклад lst2),
який містить лише змінні типу стрінг, які присутні в lst1.
Данні в лісті можуть бути будь якими"""

print('-' * 20 + ' Рішення ' + '-' * 20)
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for element in lst1:
    if isinstance(element, str):
        lst2.append(element)

lst3 = [element for element in lst1 if isinstance(element, str)]

print(f"Перший спосіб: {lst2}")
print(f"Другий спосіб: {lst3}")
