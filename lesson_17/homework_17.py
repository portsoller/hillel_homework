# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
print('ЗАВДАННЯ 1:')
def check_even_number(n):
    for num in range(n + 1):
        if num % 2 == 0:
            yield num

print(list(check_even_number(12)))

# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
print('ЗАВДАННЯ 2:')
def fibonacci_generator(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

print(list(fibonacci_generator(15)))

# Реалізуйте ітератор для зворотного виведення елементів списку.
print('ЗАВДАННЯ 3:')
def reverse_iterator(my_list):
    # for item in range(len(my_list) - 1, -1, -1): перший спосіб
    #     yield my_list[item]
    for item in my_list[::-1]:
        yield item

my_list = [1, 2, 3, 4, 5]
iter = reverse_iterator(my_list)
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))

# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
print('ЗАВДАННЯ 4:')
def iterator(n):
    for item in range(0, n + 1, 2):
        yield item

iter2 = iterator(16)

print(next(iter2))
print(next(iter2))
print(next(iter2))
print(next(iter2))
print(next(iter2))
print(next(iter2))
print(next(iter2))
print(next(iter2))
print(next(iter2))

# Напишіть декоратор, який логує аргументи та результати викликаної функції.
print('ЗАВДАННЯ 5:')
import logging
logging.basicConfig(level=logging.INFO)

def log_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(f"Функція {func.__name__} викликана з аргументами args={args}, kwargs={kwargs}. "
                     f"Результат: {result}")
        return result
    return wrapper

@log_decorator
def sum_numbers(a, b):
    result = a + b
    return result

sum_numbers(1, 2)
sum_numbers(a=3, b=5)

# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
print('ЗАВДАННЯ 6:')
def calc_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Виникла помилка під час виконання функції: {e}")
    return wrapper

@calc_decorator
def divide_numbers(a, b):
    result = a / b
    return result

divide_numbers(6, 'test')
