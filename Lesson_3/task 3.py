#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_fun(var_1, var_2, var_3):
    return(sum(sorted([var_1, var_2, var_3])[1:]))

print(my_fun(20, 4, 6))

