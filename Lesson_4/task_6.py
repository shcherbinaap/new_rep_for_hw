# 6. Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

from itertools import count, cycle

user_num = input("Введите начальное, конечное и число повторений последовательности через пробел: ")
user_num_list = user_num.split()
num_list = []
try:
    start_count = int(user_num_list[0])
    stop_count = int(user_num_list[1])
    num_count = int(user_num_list[2])
    for el in count(start_count):
        print(el)
        num_list.append(el)
        if el > stop_count - 1:
            break

    print()
    # my_list = [1, 2, 3]
    count = 0
    for i in cycle(num_list):
        print(i)
        count += 1
        if count > num_count - 1:
            break

except ValueError:
    print("Одно из значений не число!")
except IndexError:
    print("Введите три числа!")


