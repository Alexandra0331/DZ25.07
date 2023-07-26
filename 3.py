# 3. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.


import random

a = {'matches': 0, 'thermos': 1, 'tent': 7, 'food': 5, 'compass': 1, 'water': 2, 'flashlight': 1,
     'sleeping bag': 1, 'map': 0, 'first aid kit': 1}

max_weight = 15
counter = 0
List_thing = []
while counter < max_weight:
    key, value = random.choice(list(a.items()))
    if key in List_thing:
        continue
    if counter + value > max_weight:
        break
    counter += value
    List_thing += (str(key), str(value))

print(List_thing, "=", counter)