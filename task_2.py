class Road:
    _length = None
    _width = None
    _thickness = None

    def __init__(self, length, width, thickness):
        self._length = length
        self._width = width
        self._thickness = thickness
    # метод выводит результат в тоннах

    def asphalt_cons(self):
        consumption = (self._length * self._width * (self._thickness / 100) * 25) / 1000
        print(f'Вам потребуется {consumption} тонн асфальта')
        return consumption


a = Road(5000, 20, 5)
b = Road(1000, 30, 10)
print(a.asphalt_cons())
print(b.asphalt_cons())
