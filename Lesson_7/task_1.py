# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __str__(self):
        new_str = ""
        for i in self.list_of_list:
            for j in i:
                new_str = f"{new_str}{j}\t"
            new_str = f"{new_str}\n"
        return new_str

    def max_str(self):
        return len(self.list_of_list)

    def max_col(self):
        col_count = 0
        for i in range(len(self.list_of_list)):
            if col_count < len(self.list_of_list[i]):
                col_count = len(self.list_of_list[i])
        return col_count

    def martrix_format(self, max_str, max_col):
        while len(self.list_of_list) != max_str:
            if len(self.list_of_list) < max_str: self.list_of_list.append([])
        for i in range(max_str):
            while len(self.list_of_list[i]) != max_col:
                if len(self.list_of_list[i]) < max_col: self.list_of_list[i].append(0)
        return self.list_of_list

    def __add__(self, other):
        new_matrix_global = []
        max_str, max_col = max(self.max_str(), other.max_str()), max(self.max_col(), other.max_col())
        self.martrix_format(max_str, max_col)
        other.martrix_format(max_str, max_col)
        for i in range(max_str):
            new_matrix_local = []
            for j in range(max_col):
                new_matrix_local.append(self.list_of_list[i][j] + other.list_of_list[i][j])
            new_matrix_global.append(new_matrix_local)
        return new_matrix_global


mat_1 = Matrix([[1, 2], [], [3, 4, 5, 6]])
mat_2 = Matrix([[5, 6], [7, 8], [9, 10], [11, 12]])
# print(mat_1)

mat_3 = Matrix(mat_1 + mat_2)
print(mat_3)
