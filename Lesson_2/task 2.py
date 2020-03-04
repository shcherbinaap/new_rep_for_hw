#2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

# Вариант 1. Список формируется пользователем по элементно
my_list = []
lenght_my_list = int(input("Введите количество элементов списка: "))

for j in range(lenght_my_list):
    elem = input("Введите {} элемент списка: ".format(j + 1))
    my_list.append(elem)


print(f"Список до преобразования: {my_list}")
for i in range(len(my_list)):
    if i % 2 == 1:
        my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]

print(f"Список после преобразования: {my_list}")

# Вариант 2. пользователь задает строку и из нее получает список

user_str = input("Введите текст: ")
my_list = user_str.split()
print(my_list)

print(f"Список до преобразования: {my_list}")
for i in range(len(my_list)):
    if i % 2 == 1:
        my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]

print(f"Список после преобразования: {my_list}")
