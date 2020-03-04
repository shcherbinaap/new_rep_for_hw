#5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

from sys import exit

def inp_num(sum):
    while True:
        num = input(f"Введите числа через пробел или 'q' для выхода: ")
        num_list =[]
        if num.lower() == "q":
            print(sum)
            exit()
        try:
            num_list = num.split()
            for i in range(len(num_list)):
                num_list[i] = float(num_list[i])
            return num_list
        except ValueError:
            print("Введено не число!")

def sum_var(list, sum):
    for i in list:
        sum += i
    return sum

sum = 0

while True:
    sum = sum_var(inp_num(sum), sum)
    print(sum)