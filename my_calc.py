import sys

def plus(x, y):
    return x + y


def minus(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        print('Делить на ноль нельзя!')
        sys.exit()

