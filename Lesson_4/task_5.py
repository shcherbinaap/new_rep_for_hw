# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce
range_min = 100
range_max = 1001

my_list = [el for el in range(range_min, range_max) if el % 2 == 0]
pow_my_list = reduce(lambda x, y: x * y, my_list)

print(my_list)
print(pow_my_list)
