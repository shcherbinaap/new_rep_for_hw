# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class My_error(Exception):
    def __init__(self, txt):
        self.txt = txt

user_var = input("Введите делитель: ")

try:
    user_var = float(user_var)
    if user_var == 0:
        raise My_error("Вы ввели 0! На 0 делить нельзя!!!")
except ValueError:
    print("Вы ввели не число")
except My_error as err:
    print(err)
else:
    print(1000 / user_var)
