from random import randint


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'машина {self.name} остановилась')

    def turn(self, direction):
        if direction == 'right':
            print(f'машина {self.name} повернула направо')
        elif direction == 'left':
            print(f'машина {self.name}  повернула налево')
        else:
            print('неверно задано направление')

    def show_speed(self):
        print(f'текущая скорость автомобиля {self.name} {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Так-так, превышаем?')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Рабочая машина превысила скорость')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


lacetti = TownCar(70, 'yellow', 'chevrolet', False)
lacetti.show_speed()
kamaz = WorkCar(60, 'black', 'truck', False)
kamaz.show_speed()
patrol = PoliceCar(100, 'blue', 'bobik', True) # знаю что транслитом нельзя писать, лучше бобика ничего не придумал
patrol.go()
patrol.turn('right')
patrol.stop()
lambo = SportCar(200, 'red', 'lamborghini', False)
lambo.show_speed()