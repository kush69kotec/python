from abc import ABC, abstractmethod


class AbsClass(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def consumption(self):
        pass


class Clothes(AbsClass):
    def __init__(self, title):
        super().__init__()
        self.title = title


class Coat(Clothes):
    def __init__(self, title, size):
        super().__init__(title)
        self.v = size

    @property
    def consumption(self):
        cons = round((self.v / 6.5) + 0.5, 2)
        return cons


class Suit(Clothes):
    def __init__(self, title, height):
        super().__init__(title)
        self.h = height

    @property
    def consumption(self):
        cons = round((self.h * 2) + 0.3, 2)
        return cons


coat = Coat('brioni', 80)
suit = Suit('zegna', 180)

print(coat.consumption)
print(suit.consumption)

print(f'{coat.consumption + suit.consumption} - общий расход ткани')