# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

out_f = open("file_task_1.txt", "w", encoding="utf-8")
while True:
    str = input("Введите текс для записи в файл, пустая строка конец записи: ")
    if str == "" or str == " ":
        break
    out_f.writelines(str + "\n")

out_f.close()
