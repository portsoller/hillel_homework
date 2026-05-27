python_students = {"Олексій", "Марія", "Ярослав", "Олена", "Дмитро"}
qa_students = {"Ярослав", "Олена", "Ірина", "Максим", "Дмитро"}

# Завдання 1.1: "Універсальні бійці"
# Знайди студентів, які одночасно навчаються і на курсі Python, і на курсі QA.
print('-' * 20 + ' Рішення 1.1 ' + '-' * 20)
logical_intersection = python_students & qa_students
# або logical_intersection = python_students.intersection(qa_students)
print(logical_intersection)

#
# Завдання 1.2: "Списки на розсилку"
# Адміністрації академії потрібно зібрати повний список усіх унікальних студентів обох курсів, щоб надіслати їм спільне оголошення. Дублікатів імен у списку бути не повинно.
print('-' * 20 + ' Рішення 1.2 ' + '-' * 20)
logical_union = python_students.union(qa_students)
# або logical_union = python_students | qa_students
print(logical_union)
#
# Завдання 2.1: "Суто програмісти"
# Знайди студентів, які вчать Python, але взагалі не цікавляться курсом QA.
print('-' * 20 + ' Рішення 2.1 ' + '-' * 20)
logical_difference = python_students.difference(qa_students)
# або logical_difference = python_students - qa_students
print(logical_difference)

#Завдання 2.2: "Тільки один курс"
# Знайди студентів, які обрали для себе тільки один напрямок (або суто Python, або суто QA), тобто виключи тих, хто ходить на обидва курси одночасно.
print('-' * 20 + ' Рішення 2.2 ' + '-' * 20)
logical_symmetric_difference = python_students.symmetric_difference(qa_students)
# або logical_symmetric_difference = python_students ^ qa_students
print(logical_symmetric_difference)

active_users = [101, 102, 105, 107, 110, 120]
premium_users = [102, 105, 110, 115, 130]
churned_users = [105, 140, 115]
# Завдання 3: "Аналітика SaaS-платформи" (Велика задача)
# Уяви, що ти працюєш над SaaS-платформою. У тебе є три списки ID користувачів:
#
# active_users — ті, хто заходив на платформу цього місяця.
#
# premium_users — ті, хто купив преміум-підписку.
#
# churned_users — ті, хто написав у саппорт і видалив акаунт.

# Тобі потрібно написати код, який відповість на 3 питання бізнесу:
#

print('-' * 20 + ' Рішення 3 ' + '-' * 20)
# Переводим списки из условия в сеты
active_set = set(active_users)
premium_set = set(premium_users)
churned_set = set(churned_users)

# Які преміум-користувачі були активними цього місяця? (Кому не дарма капає підписка).
logical_intersection = active_set.intersection(premium_set)
# або logical_intersection = active_set & premium_set
print(f"{logical_intersection} - преміум-користувачі були активними цього місяця")

# Які преміум-користувачі взагалі не заходили на платформу? (Їм треба надіслати email-нагадування, бо вони скоро скасують підписку).
logical_difference = premium_set.difference(active_set)
# або logical_difference = premium_set - active_set
print(f"{logical_difference} - преміум-користувачі які взагалі не заходили на платформу цього місяця")

# Чи є серед активних користувачів ті, хто вже офіційно вважається видаленим (churned_users)? (Якщо є, то це критичний баг у базі даних!).
logical_intersection = churned_set.intersection(active_set)
# або logical_difference = churned_set & active_set
print(f"{logical_intersection} - активні користувачі, хто вже офіційно вважається видаленим")