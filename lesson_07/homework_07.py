# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 5:
        result = number * multiplier
        # десь тут помилка, а може не одна
        if  result > 25:
            break # Enter the action to take if the result is greater than 25
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
print('-' * 20 + ' Solution task 2' + '-' * 20)
def sum_num(num_1: float, num_2: float):
    return num_1 + num_2

print(f"The result is: {sum_num(1, 2)}")

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
print('-' * 20 + ' Solution task 3' + '-' * 20)

lst = [2, 5, 7, 10, 15, 20]
def avg_value(lst):
    return sum(lst) / len(lst)

print(f"The average value is: {avg_value(lst)}")

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
print('-' * 20 + ' Solution task 4' + '-' * 20)

def reverse_string(string):
    return string[::-1]

print(reverse_string('blablabla'))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
print('-' * 20 + ' Solution task 5' + '-' * 20)

words = ['Best', 'Tost', 'QA', 'Audi', 'Lesson', 'Attribute', 'Elementary']
def largest_word(words):

    word_lengths = max(words, key=len)
    return word_lengths
print(largest_word(words))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
print('-' * 20 + ' Solution task 6' + '-' * 20)

def find_substring(str1, str2):
        return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
# task 7
print('-' * 20 + ' Solution task 7' + '-' * 20)

def find_perimeter(side1, side2, side3, side4):
    """
    Функція рахує периметр фігури.
    :param side1: довжина першої сторони
    :param side2: довжина другої сторони
    :param side3: довжина третьої сторони
    :param side4: довжина четвертої сторони
    :return: Виводить периметр фігури
    """
    return side1 + side2 + side3 + side4
print(find_perimeter(2, 4, 2, 4))

# task 8
print('-' * 20 + ' Solution task 8' + '-' * 20)

def change_a_space(string):
    """
    Функція має замінювати в тексті символи .... на один пробіл
    :param string: тут приймає на вхід текст
    :return: на виході віддає той самий текст, лиш з пробілами замість '....'
    """
    return string.replace("....", " ")
print(change_a_space('Tom gave up the brush with reluctance in his .... face but alacrity in his heart'))

# task 9
print('-' * 20 + ' Solution task 9' + '-' * 20)

def words_count(sentence):
    """
    Функція виводить кількість слів з речення
    :param sentence: Одне речення
    :return: Кількість слів
    """
    return len(sentence.split())

print(f"The number of words: {words_count('Hello, world!')}")

# task 10
print('-' * 20 + ' Solution task 10' + '-' * 20)
def try_to_find_h(string):
    """
    Перевіряє наявність літери 'h' в переданому рядку, любого регістру
    :param string: Стрічка для перевірки
    :return: "Letter 'H' was found"
    """

    if 'h' in string.lower():
        return "Letter 'H' was found"
    else:
        return "Letter 'H' was NOT found"

print(try_to_find_h("Hello, world!"))
print(try_to_find_h("Audi"))