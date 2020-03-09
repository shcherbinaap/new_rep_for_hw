# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fibo_gen().
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

def generator(max_num):
    for el in range(1, max_num + 1):
        yield el


max_num = 16  # Максимальное значение факториала
max_count = 15  # Значение ограничения вычисления факториала

pow = 1
count = 0
for el in generator(max_num):
    if count >= max_count:
        break
    pow *= el
    count += 1

print(pow)