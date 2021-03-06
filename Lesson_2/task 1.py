#1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = ["Строка", (1, 2), 1, 10.5]

# Вариант 1. Через while
print("Вариант №1")
i = 0
while i < len(my_list):
    print(f"Тип {i + 1} элемента списка {type(my_list[i])}")
    i += 1


# Вариант 2. Через for, когда нужна информация об индексе
print("Вариант №2")
my_list_type = []
for i in range(len(my_list)):
    print(f"Тип {i + 1} элемента списка {type(my_list[i])}")
    my_list_type.append(type(my_list[i]))

print(my_list_type)

# Вариант 3. Через for, когда информация об индексе не нужна
print("Вариант №3")
for item in my_list:
    print(f"Тип элемента списка '{item}' - {type(item)}")

    