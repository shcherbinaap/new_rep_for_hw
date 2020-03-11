# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint


def write_file(file_name, text):
    out_f = open(file_name, "w", encoding="utf-8")
    out_f.write(text)
    out_f.close()


def read_file(file_name, all = True):
    my_f = open(file_name, "r", encoding="utf-8")
    if all == True:
        content = my_f.read()
    else:
        content = my_f.readlines()
    my_f.close()
    return content


def rand_num_list(quantity):
    count = 0
    rand_list = []
    while True:
        if count >= quantity:
            break
        rand_list.append(randint(0, 10))
        count += 1
    return rand_list


def rand_num_str(quantity, sep):
    count = 0
    rand_str = ""
    while True:
        if count >= quantity:
            break
        rand_str = f"{rand_str}{randint(0, 10)}{sep}"
        count += 1
    return rand_str


def str_to_int(user_list):
    new_list = []
    for i in range(len(user_list)):
        try:
            new_list.append(int(user_list[i]))
        except ValueError:
            # pass
            print("Значение не может быть переведено в число, оно удалено!")
    return new_list

if __name__ == "__main__":
    var_to_file = f"{rand_num_str(5, ' ')}\n{rand_num_str(6, ' ')}"
    print(var_to_file)
    write_file("file_task_5.txt", var_to_file)

    var_from_file = sum(str_to_int(read_file("file_task_5.txt").split()))

    print(var_from_file)
