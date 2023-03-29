# 1 41 54

"""
3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
"""

my_list = ['a', 'b', [1, 2, 3], 'd']
print(*my_list[2], sep=', ')

"""
3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
   - получите сумму всех чисел,
   - распечатайте все строки, где есть буква 'a'
"""

list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
numbers = [list_1[i] for i in range(len(list_1)) if isinstance(list_1[i], int)]
print(sum(numbers))
print(*[list_1[i] for i in range(len(list_1)) if isinstance(list_1[i], str) and 'a' in list_1[i]])

"""
3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
"""

pets = ['cat', 'dog', 'horse', 'cow']
pets_tuple = tuple(pets)
print(pets_tuple)

"""
3.4. Напишите программу, которая определяет, какая семья больше.
      1) Программа имеет два input() - например, family_1, family_2.
      2) Членов семьи нужно перечислить через запятую.
     Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
"""

family_1, family_2 = list(input('Введите членов первой семьи через запятую: ').split(',')), \
                     list(input('Введите членов второй семьи через запятую: ').split(','))
if len(family_1) > len(family_2):
    print(family_1)
elif len(family_1) == len(family_2):
    print('Equal')
else:
    print(family_2)

"""
3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
    о вашем любимом фильме.
    - распечатайте только ключи
    - распечатайте только значения
    - распечатайте пары ключ - значение

"""

film = {'title': 'Spirit: Stallion of the Cimarron', 'director': 'Келли Эсбери', 'year': '2002',
        'budget': '80 million dollar', 'main_actor': 'Spirit <3', 'slogan': 'Some legends can never be tamed'}
print(film.keys())
print(film.values())
print(film.items())

"""
3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
"""

my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}

print(sum(my_dictionary.values()))

"""
3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
"""

spisok = [1, 2, 3, 4, 5, 3, 2, 1]
print(list(set(spisok)))

""""
3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
     - найдите значения, которые встречаются в обоих множествах
     - найдите значения, которые не встречаются в обоих множествах
     - проверьте являются ли эти множества подмножествами друг друга 
"""

set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
spisok1 = list(set1)
spisok2 = list(set2)
spisok = []
spisok3 = []

for i in range(len(spisok1)):
    if spisok1[i] in spisok2:
        spisok.append(spisok1[i])
    else:
        spisok3.append(spisok1[i])

for i in range(len(spisok2)):
    if spisok2[i] not in spisok:
        spisok3.append(spisok2[i])

print(*spisok)
print(*spisok3)

print(set1.intersection(set2))          # из урока
print(set1.symmetric_difference(set2))  # из урока

print(set1.issubset(set2))
print(set2.issubset(set1))
