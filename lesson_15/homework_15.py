"""
Завдання 1:
Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх.
Результат запишіть у файл result_<your_second_name>.csv
"""
from pathlib import Path

CURRENT_DIR = Path(__file__).parent
csv_dir = CURRENT_DIR / 'work_with_csv'

import csv

file1_path = csv_dir / 'random.csv'
file2_path = csv_dir / 'random-michaels.csv'
result_path = csv_dir / 'result_abramenko.csv'

# Сюда соберем все уникальные строки
all_data = []

# 1. Читаем первый файл полностью
with open(file1_path, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        all_data.append(row)  # Добавляем всё, включая заголовок

# 2. Читаем второй файл и добавляем только уникальные строки
with open(file2_path, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Пропускаем заголовок второго файла, он нам не нужен

    for row in reader:
        # Проверяем: если такой строки еще нет в нашем списке, добавляем её
        if row not in all_data:
            all_data.append(row)

# 3. Записываем результат (один в один как во втором примере конспекта)
with open(result_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(all_data)  # Записывает весь наш массив данных за раз

"""
Завдання 2:
Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json. 
результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log
"""
import json
import logging
from pathlib import Path

json_logger = logging.getLogger('json_validator')
json_logger.addHandler(logging.FileHandler('json__abramenko.log', encoding='utf-8'))

CURRENT_DIR = Path(__file__).parent
json_dir = CURRENT_DIR / 'work_with_json'
files = [f for f in json_dir.iterdir() if f.is_file()]

for file in files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        json_logger.error(f"Файл {file.name} не є валідним JSON. Помилка: {e}")

"""
Завдання 3:
Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і 
повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо
"""

import logging
import xml.etree.ElementTree as ET

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

tree = ET.parse('groups.xml')
root = tree.getroot()

def get_group_details(group_number):
    for group in root.findall('group'):
        group_number_element = group.find('number')
        if group_number_element is not None and group_number_element.text == group_number:
            timing_exbytes = group.find('timingExbytes')
            if timing_exbytes is not None:
                incoming = timing_exbytes.find('incoming')
                if incoming is not None:
                    logging.info(f"Group: {group.find('name').text}, incoming: {incoming.text}")
                    return incoming.text
                else:
                    logging.info(f"Group: {group.find('name').text}, incoming: Не знайдено")
                    return None
            else:
                logging.info(f"Group: {group.find('name').text}, timingExbytes не знайдено")
                return None

    logging.warning(f"The group with a number {group_number} does not found!")
    return None

get_group_details("2")
