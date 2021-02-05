log = """name:Иван;gender:m;item:Часы;item_cost:9800
name:Иван;gender:m;item:Фитнес-браслет;item_cost:12300
name:Иван;gender:m;item:Кофемашина;item_cost:23500
name:Петр;gender:m;item:Часы;item_cost:9800
name:Петр;gender:m;item:Фитнес-браслет;item_cost:12300
name:Петр;gender:m;item:Айфон;item_cost:77900
name:Петр;gender:m;item:Чехол для телефона;item_cost:350
name:Петр;gender:m;item:Кофемашина;item_cost:23500
name:Дарья;gender:m;item:Айфон;item_cost:77900
name:Марья;gender:m;item:Кофемашина;item_cost:23500
name:Юлия;gender:m;item:Фитнес-браслет;item_cost:12300"""


# Делим данные log на список строк по разделителю - перенос строки
elements = log.split('\n')

# Создаем две переменные. В item_names будут передаваться значения item, а в item_numbers элементы из item_cost
item_names = []
item_numbers = []

# Проходимся циклом по elements, разбиваем данные по точке с запятой и оставляем элементы из item и item_cost
for i in elements:
    elements_list = i.split(';')[2:4]
    
    # Убираем слова item и item_cost
    elements_list2 = [a.split(':')[1] for a in elements_list]
    
    # Передаём наименования товаров в переменную item_names, а стоимость товаров в переменную item_numbers
    item_names.append(elements_list2[0])
    item_numbers.append(int(elements_list2[1]))

# Создаём словарь. В качестве ключа используются наименования товаров, в качестве значений - стоимость
names_numbers = dict(zip(item_names, item_numbers))

item_list = []

# Обходим словарь по элементам. Если стоимость < 13000, то передаём в item_list наименования товаров, цена по которым < 13000
for k, v in names_numbers.items():
    if v < 13000:
        item_list.append(k)
print(item_list)