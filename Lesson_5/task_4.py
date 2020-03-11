# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

my_f = open("file_task_4_1.txt", "r", encoding="utf-8")

content_line = my_f.readlines()

my_dict = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}
str = ""

for el in content_line:
    el = el.split()
    str = str + f"{my_dict[el[0]]} - {el[2]}\n"
print(str)

out_f = open("file_task_4_2.txt", "w", encoding="utf-8")
out_f.writelines(str)
out_f.close()
my_f.close()