class Cell:
    def __init__(self, num_of_cells):
        self.num_of_cells = int(num_of_cells)

    def __str__(self):
        return str(self.num_of_cells)

    def __add__(self, other):
        if isinstance(other, Cell):
            return Cell(self.num_of_cells + other.num_of_cells)
        else:
            raise ValueError('Нельзя произвести сложение')

    def __sub__(self, other):
        if isinstance(other, Cell) and self.num_of_cells > other.num_of_cells:
            return Cell(self.num_of_cells - other.num_of_cells)
        else:
            raise ValueError('Нельзя произвести вычитание')

    def __mul__(self, other):
        if isinstance(other, Cell):
            return Cell(self.num_of_cells * other.num_of_cells)
        else:
            raise ValueError('Нельзя произвести умножение')

    def __floordiv__(self, other):
        if isinstance(other, Cell):
            return Cell(self.num_of_cells // other.num_of_cells)
        else:
            raise ValueError('Нельзя произвести деление')

    def make_order(self, cells_in_row):
        res_str = ''
        for _ in range(self.num_of_cells // cells_in_row):
            res_str += f'{cells_in_row * "*"}\n'
        res_str += '*' * (self.num_of_cells % cells_in_row)
        return res_str


a = Cell(15)
b = Cell(7)
c = a * b
print(c)
print(c.make_order(10))
