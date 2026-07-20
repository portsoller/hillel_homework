"""
Моніторингова система клєнта надсилає сигнал, що вона працездатна кожні 30-31 сек -
наприкладTimestamp 05:45:40, а в наступному повідомлені — Timestamp 05:45:09 (тут різниця heartbeat в 31 секунду)
Є декілька дублючих потоків, що шлють дані одночасно, тож ми можемо проаналізувати лише один потік -
Key TSTFEED0300|7E3E|0400

Засобами автоматизації проаналізуйте наданий нам лог: hblog.txt

відберіть лише строки з вказаним ключем Key TSTFEED0300|7E3E|0400
Створіть функцію, що поверне лог-файл, де буде аналіз правильності вимог:
для кожного випадку де heartbeat більше 31 сек але менше 33 логувало WARNING в файл hb_test.log
для кожного випадку де heartbeat більше рівно 33 логувало ERROR в файл hb_test.log
       3.Зверніть увагу, що нам для аналізу помилок було б добре знати час, в який помилка відбулася.

Обов’язково включіть результат роботи — файл hb_test.log в PR.

Підказка 1

Прочитайте файл по строкам, якщо забули як - зверніться до 12 лекції.
Виберіть строки з необхідним значенням:
filtered_log = []
if "key" in "long log string with key":
    filtered_log.append("long log string with key")

Підказка 2

Пошук часу у строці можна зробити методом .find("Timestamp ") і повернути наступні 8 символів
перетворити строку в час дозволяє метод .strptime("10:00:00", "%H:%M:%S")
Значення слід аналізувати парами - від поточного відняти наступне і залогувати (або не залогувати) результат
"""
from datetime import datetime, timedelta

def monitoring_system():
    filtered_lines = []
    with open('hblog.txt', 'r') as f:
        content = f.readlines()

    for line in content:
        if "TSTFEED0300|7E3E|0400" in line:
            filtered_lines.append(line)
    return filtered_lines

result_lines = monitoring_system()
timestamps = []
for line in result_lines:
    index = line.find("Timestamp ")
    time_str = line[index + 10 : index + 18]
    t_struct = datetime.strptime(time_str, "%H:%M:%S")
    timestamps.append(t_struct)

with open('hb_test.log', 'w') as f:
    for i in range(len(timestamps) - 1):
        current_time = timestamps[i]
        next_time = timestamps[i + 1]
        time_difference = current_time - next_time
        seconds = time_difference.total_seconds()
        if seconds >= 33:
            f.write(f"ERROR {current_time.strftime("%H:%M:%S")}\n")
        elif seconds > 31 and seconds < 33:
            f.write(f"WARNING {current_time.strftime("%H:%M:%S")}\n")
