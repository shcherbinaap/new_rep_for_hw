# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

my_f = open("file_task_3.txt", "r", encoding="utf-8")
content = my_f.read()
str_count = content.split("\n")
print(str_count)

min_income = 20000.0
mean_income = 0
user_loss = []
user_loss_str = ""
income = []

for el in str_count:
    el = el.split()
    if float(el[2]) <= min_income:
        user_loss.append(el[1])
        user_loss_str = user_loss_str + el[1] + " "
    income.append(float(el[2]))


print(f"Список сотрудников получающих меньше {min_income} - {user_loss}")
print(f"Список сотрудников (строкой) получающих меньше {min_income} - {user_loss_str}")
print(f"Средний доход составляет: {sum(income)/len(str_count)})")
my_f.close()