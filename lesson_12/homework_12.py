
def sum_num(num_1: float, num_2: float):
    return num_1 + num_2

def avg_value(lst):
    return sum(lst) / len(lst)

def reverse_string(string):
    return string[::-1]

def words_count(sentence):
    """
    Функція виводить кількість слів з речення
    :param sentence: Одне речення
    :return: Кількість слів
    """
    return len(sentence.split())
