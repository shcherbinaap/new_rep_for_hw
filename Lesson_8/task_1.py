# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, date: str):
        self.date = date

    @classmethod
    def str_to_list_int(cls, string: str):
        list_date = [int(el) for el in string.split("-")]
        return list_date

    @staticmethod
    def valid_date(list_date):
        day_in_month = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }
        if list_date[2] % 4 == 0:
            day_in_month[2] = 29
        if day_in_month.get(list_date[1]) == None:
            print("В веденной дате месяц введен не верно!")
        elif list_date[0] < 1 or list_date[0] > day_in_month[list_date[1]]:
            print("Число в дате введено вне диапазона")


my_str = "29-02-2001"
Data.valid_date(Data.str_to_list_int(my_str))
