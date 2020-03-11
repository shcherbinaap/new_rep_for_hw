# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

from task_5 import read_file, write_file, str_to_int

my_str = "Фирма1 ООО 10000 15000\n" \
         "Фирма2 ИП 10000 5000\n" \
         "Фирма3 ООО 10000 10000"

write_file("file_task_7.txt", my_str)

var = read_file("file_task_7.txt", False)
firm_dict = {}
profit_dict = {}
firm_list = []
profit = 0
for el in var:
    el_list = el.split()
    try:
        profit += float(el_list[2]) - float(el_list[3])
        firm_dict[el_list[0]] = float(el_list[2]) - float(el_list[3])
    except ValueError:
        print(f"ValueError - Введено не число! Фирма '{el_list[0]}' в статистике не учитывается!")

firm_list.append(firm_dict)
profit_dict["average_profit"] = profit / (len(firm_dict))
firm_list.append(profit_dict)

with open("file_task_7.json", "w") as write_f:
    json.dump(firm_list, write_f)

