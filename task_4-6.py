class CountException(Exception):
    def __init__(self, txt):
        self.txt = txt


class OfficeWarehouse:
    def __init__(self, square, floors, address, available_dict=None):
        if available_dict is None:
            available_dict = {}
        self.title = self
        self.square = square
        self.floors = floors
        self.address = address
        self.available_dict = available_dict


class OffEquip:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def store_tech(self, office_warehouse_name, count):
        try:
            if type(count) is str:
                raise CountException('Вы ввели строковое значение')
        except CountException as err:
            print(err)
        if self.brand in office_warehouse_name.available_dict and self.model in office_warehouse_name.available_dict[
            self.brand]:
            office_warehouse_name.available_dict[self.brand][self.model] += count
        else:
            office_warehouse_name.available_dict[self.brand] = {self.model: count}

    def move_tech(self, from_office_warehouse_name, to_office_warehouse_name, count):
        from_office_warehouse_name.available_dict[self.brand][self.model] -= count
        if self.brand in to_office_warehouse_name.available_dict and self.model in \
                to_office_warehouse_name.available_dict[
                    self.brand]:
            to_office_warehouse_name.available_dict[self.brand][self.model] += count
        else:
            to_office_warehouse_name.available_dict[self.brand] = {self.model: count}


class Printer(OffEquip):
    def __init__(self, brand, year, model, is_laser, color):
        super().__init__(brand, model)
        self.year = year
        self.is_laser = is_laser
        self.color = color


class Scanner(OffEquip):
    def __init__(self, brand, year, model, color):
        super().__init__(brand, model)
        self.year = year
        self.color = color


class Xerox(OffEquip):
    def __init__(self, brand, year, model, color, speed):
        super().__init__(brand, model)
        self.year = year
        self.color = color
        self.speed = speed


main_wh = OfficeWarehouse('100', '5', 'SPB')
second_wh = OfficeWarehouse('150', '2', 'Moscow')
scx4200 = Printer('samsung', '2008', 'scx4200', True, 'white')
hl2130 = Scanner('HP', '2004', 'hl2130', 'white')
scx4200.store_tech(main_wh, 1)
hl2130.store_tech(second_wh, 5)
hl2130.move_tech(second_wh, main_wh, 2)

