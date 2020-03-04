#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
from sys import exit
def inp_num(a):
    while True:
        num = input(f"Введите число {a} или 'q' для выхода: ")
        if num.lower() == "q": exit()
        try:
            return float(num)
        except ValueError:
            print("Введено не число!")

def my_fun(num_1, num_2):
    try:
        return num_1 / num_2
    except ZeroDivisionError:
        print("Деление на 0!!!")
        exit()


print(my_fun(inp_num(1), inp_num(2)))
