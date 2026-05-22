adventures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adventures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adventures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
print('--------------------task 01------------------------')
adventures_of_tom_sawer = adventures_of_tom_sawer.replace("\n", " ")
print(adventures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
print('--------------------task 02------------------------')
adventures_of_tom_sawer = adventures_of_tom_sawer.replace("....", " ")
print(adventures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print('--------------------task 03------------------------')
# adventures_of_tom_sawer = adventures_of_tom_sawer.replace("   ", " ") # або в нашому випадку коректно працює от такий спосіб, але не гарантує результат
adventures_of_tom_sawer = " ".join(adventures_of_tom_sawer.split())
print(adventures_of_tom_sawer)


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print('--------------------task 04------------------------')
# h_counter = adventures_of_tom_sawer.lower().count('h') # або можна зробити от так
h_counter = adventures_of_tom_sawer.count('h')
print(f'Літера "h" зустрічаєтсья в тексті {h_counter} разів')

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print('--------------------task 05------------------------')
words = adventures_of_tom_sawer.split()
count = 0
for k in words:
    if k.istitle():
        count += 1
print(f"В тексті є {count} слів, що починаютсья з великої літери")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print('--------------------task 06------------------------')
first_entry = adventures_of_tom_sawer.find("Tom",0)
second_entry = adventures_of_tom_sawer.find("Tom",first_entry + 1)
print(f"Слово 'Tom' вдруге знаходиться на {second_entry} позиції")

# task 07
""" Розділіть змінну adventures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adventures_of_tom_sawer_sentences
"""
print('--------------------task 07------------------------')
adventures_of_tom_sawer_sentences = adventures_of_tom_sawer.rstrip(".").split(".")
print(adventures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adventures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print('--------------------task 08------------------------')
result = adventures_of_tom_sawer_sentences[3].lower()
print(f"Четверте речення з тексту:\n{result}")


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print('--------------------task 09------------------------')
for k in adventures_of_tom_sawer_sentences:
    result_sentence = k.strip()
    if result_sentence.startswith("By the time"):
        print(result_sentence)

# task 10
""" Виведіть кількість слів останнього речення з adventures_of_tom_sawer_sentences.
"""
print('--------------------task 10------------------------')
last_sentence = adventures_of_tom_sawer_sentences[-1].split()

print(f"Кількість слів у реченні: {len(last_sentence)}")