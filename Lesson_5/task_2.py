# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

# Вариант 1.
my_f = open("file_task_2.txt", "r", encoding="utf-8")

content = my_f.read()
str_count = content.split("\n")

print(f"Количество строк в файле: {len(str_count)}")
for i in range(len(str_count)):
    print(f"Количество слов в строке {i + 1} - {len(str_count[i].split())}")
    print(f"Количество символов в строке {i + 1} - {len(str_count[i])}")

my_f.close()

# Вариант 2. Не особо отличающийся от первого
my_f = open("file_task_2.txt", "r", encoding="utf-8")

content_line = my_f.readlines()
print(f"Количество строк в файле: {len(content_line)}")
for i in range(len(content_line)):
    print(f"Количество слов в строке {i + 1} - {len(content_line[i].split())}")
    print(f"Количество символов в строке {i + 1} - " + str(len(content_line[i].split('\n')[0])))


my_f.close()
