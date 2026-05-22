alice_in_wonderland = '''"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don't much care where ——" said Alice. 
"Then it doesn't matter which way you go," said the Cat."
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'''
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

found_quotes = []
for k in alice_in_wonderland:
    if k == "'":
        found_quotes.append(k)
print(found_quotes)
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436402
azov_sea_area = 37800
total_area = black_sea_area + azov_sea_area
print(f"Площа Чорного та Азовського морей: {total_area} км2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

total_goods = 375291
warehouse_1_and_warehouse_2 = 250449
warehouse_3_and_warehouse_2 = 222950
warehouse_3 = total_goods - warehouse_1_and_warehouse_2
warehouse_1 = total_goods - warehouse_3_and_warehouse_2
warehouse_2 = total_goods - (warehouse_3 + warehouse_1)
print(f"На першому складі розміщено {warehouse_1}, на другому складі {warehouse_2}, а на третьому {warehouse_3} товарів")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

monthly_payment = 1179
total_pc_price = monthly_payment * 18
print(f"Загальна вартість компьютера складає {total_pc_price} гривень")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

a_value = 8019 % 8
b_value = 9907 % 9
c_value = 2789 % 5
d_value = 7248 % 6
e_value = 7128 % 5
f_value = 19224 % 9
print(f"Остача від ділення чисел складає: а:{a_value}, б:{b_value}, с:{c_value}, d:{d_value}, e:{e_value}, f:{f_value}")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

big_pizza_price = 274 * 4
medium_pizza_price = 218 * 2
juice_price = 35 * 4
cake_price = 350
water_price = 21 * 3
goods_total_price = big_pizza_price + medium_pizza_price + juice_price + cake_price + water_price
print(f"Для святкування дня народження потрібно {goods_total_price} гривень")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

photos_per_page = 8
photos_amount = 232
pages_amount = photos_amount // photos_per_page
if photos_amount % photos_per_page > 0:
    pages_amount += 1

print(f"Щоб розмістити всі {photos_amount} фото, потрібно {pages_amount} сторінок в альбомі")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

full_tank = 48
full_distance = 1600
consumption_per_100 = 9
distance_count = full_distance // 100
total_fuel = distance_count * consumption_per_100
print(f"Для такої подорожі потрібно {total_fuel} літрів бензину")
tank_count = total_fuel // full_tank

if total_fuel % full_tank > 0:
    tank_count += 1

print(f"Родині потрібно {tank_count - 1}, враховуючі що з дому автівка виїхала з повним баком")
