"""
4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
     периметр квадрата, площадь квадрата и диагональ квадрата.
"""
from math import sqrt


def square(side):
    my_tuple = (2 * side, side * side, 2 * sqrt(side))
    return my_tuple


print(square(int(input('Введите сторону квадрата: '))))

"""
4.2. Напишите функцию, которая принимает произвольное количество именованных аргументов и выводит их построчно
     в формате аргумент: значение. Например:
    name: John
    last_name: Smith
    age: 35
    position: web developer
"""


def info(**names):
    for name, value in names.items():
        print(f"{name}: {value}")


info(name='John', last_name='Smith', age=35, position='web developer')

"""
4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
     положительные числа
"""

my_list = [20, -3, 15, 2, -1, -21]

print(list(filter(lambda positive: positive >= 0, my_list)))

"""
4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
"""

from functools import reduce

my_list = [20, -3, 15, 2, -1, -21]

print(reduce(lambda x, y: x * y, my_list))

"""
4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
"""

import time


def time_work(func):
    def wrapper():
        start = time.perf_counter()
        func()
        time.sleep(3)
        end = time.perf_counter()
        print(end - start)
    return wrapper()


@time_work
def time_counter():
    print('Время выполнения функции = ', end='')


"""
4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
     Примените эти функции в качестве методов в другом файле.
"""

import my_calc

print(my_calc.division(5, 4))
