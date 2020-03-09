# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.

task_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

my_list = []
my_list_1 = []

for i in range(1, len(task_list)):
    if task_list[i - 1] < task_list[i]:
        my_list.append(task_list[i])

my_list_1 = [task_list[i] for i in range(1, len(task_list)) if task_list[i - 1] < task_list[i]]
print(my_list)
print(my_list_1)
