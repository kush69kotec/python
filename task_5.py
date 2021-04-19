class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки. Использован инстремент {self.title}')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки чернилами, тонкой линией. Использован инстремент {self.title}')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки грифелем. Использован инстремент {self.title}')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки толстой линией. Использован инстремент {self.title}')


feather = Stationery('feather')
feather.draw()
parker = Pen('parker pen')
parker.draw()
constructor = Pencil('HB pencil')
constructor.draw()
bic = Handle('bic handle')
bic.draw()
