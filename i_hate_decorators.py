# Завдання 1 Створіть функцію відображення поточного часу.
# Функція не приймає параметри та не використовує
# синтаксис декораторів. Зробіть декорування функції за
# допомогою іншої функції. Потенційне виведення даних на
# екран:
# ***************************
# 23:00
# ***************************
# У цьому виведенні на екран дві лінії із зірочок —
# результати декорування


import datetime


# def func_decorator(func):
#     def wrapper():
#         print('***************************')
#         func()
#         print('***************************')
#
#     return wrapper()
#
#
# a = datetime.datetime.now()
#
#
# def func():
#     print(f'Time - {a.time()}')
#
#
# f = func_decorator(func)


# Завдання 2 Додайте ще одну функцію для декорування
# виводу даних. Ця функція має додати нові елементи у
# форматування виводу.

def func_decorator(func):
    def wrapper():
        print('***************************')
        func()
        print('***************************')

    def wrapper2():
        func()
        print('hello')
        return wrapper2()

    return wrapper()


a = datetime.datetime.now()
b = datetime.datetime.year


def func1():
    print(f'Year - {a}')


def func():
    print(f'Time - {a.time()}')


f = func_decorator(func)
r = func_decorator(func1)
