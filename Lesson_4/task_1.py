# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, work_hour, hour_cost, bonus = argv

try:
    work_hour = float(work_hour)
    hour_cost = float(hour_cost)
    bonus = float(bonus)
    print(f"Заработная плата сотрудника составляет: {(work_hour * hour_cost) + bonus}")
except ValueError:
    print("Введены не числовые данные!")
