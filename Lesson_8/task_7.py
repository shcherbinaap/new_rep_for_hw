# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class Complex_num:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        return(f"{self.re} + i * {self.im}")

    def __add__(self, other):
        return (f"{self.re + other.re} + i * {self.im + other.im}")

    def __mul__(self, other):
        return (f"{self.re * other.re - self.im * other.im} + i * {self.im * other.re + self.re * other. im}")


a = Complex_num(2, 4)
b = Complex_num(3, 9)
print(a)
print(a.__add__(b))
print(a.__mul__(b))

