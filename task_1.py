class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = []
        for row in matrix_list:
            self.matrix_list.append(row)

    def __str__(self):
        matrix_str = ''
        for row in self.matrix_list:
            row_str = ''
            for el in row:
                row_str += f'{el}\t'
            matrix_str += f'{row_str}\n'
        return matrix_str

    def __add__(self, other):
        if isinstance(other, Matrix) and len(self.matrix_list) == len(other.matrix_list) and len(
                self.matrix_list[0]) == len(other.matrix_list[0]):
            result = self.matrix_list
            d = other.matrix_list
            for i in range(len(self.matrix_list)):
                for i_scnd in range(len(self.matrix_list[0])):
                    result[i][i_scnd] += d[i][i_scnd]
            return Matrix(result)
        else:
            return f'Второй объект не является экземпляром класса или матрицы разного размера\nВ задании нужно ' \
                   f'сложить объекты класса, а так тут можно реализовать другую логику'


a = Matrix([[3, 5, 32, 10], [2, 4, 6, 4], [-1, 64, -8, 5]])
b = Matrix([[5, 10, 16, 11], [5, 8, 12, 2], [5, 10, 5, 65]])
print(a)
print(b)
print(a + b)
