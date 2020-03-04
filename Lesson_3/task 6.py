# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_fun(str):
    return str.title()

def str_title(str):
    str_list = str.split()
    str = ""
    for i in range(len(str_list)):
        str_list[i] = int_fun(str_list[i])
        str = str + str_list[i] + " "
    return str


print(str_title("gfsadf asdfdsf adsfasdf fasdf asdf"))