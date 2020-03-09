# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

range_min = 20
range_max = 240
num_1 = 20
num_2 = 21

num_list = [i for i in range(range_min, range_max + 1) if i % num_1 == 0 or i % num_2 == 0]
num_tuple = (i for i in range(range_min, range_max + 1) if i % num_1 == 0 or i % num_2 == 0)
print(num_list)
print(num_tuple)
