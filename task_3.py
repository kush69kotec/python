class Worker:

    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self.income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def __init__(self, name, surname, wage, bonus):
        super().__init__(name, surname, wage, bonus)

    def get_full_name(self):
        print(f'Сотрудника зовут {self.name} {self.surname}')
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        print(f'Сотрудник {self.name} {self.surname} может заработать {self.income["wage"] + self.income["bonus"]}')
        return self.income['wage'] + self.income['bonus']


a = Position('Pupa', 'Pupin', 50000, 15000)
b = Position('Lupa', 'Lupin', 60000, 18000)
c = Position('Arkadiy', 'Shtirka', 30000, 5000)

c.get_full_name()
b.get_total_income()
