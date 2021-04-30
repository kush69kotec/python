import re


class Date:

    date_str = None

    def __init__(self, date_str):
        Date.date_str = date_str

    @classmethod
    def format_date(cls):
        NEW_DATE_STR = re.compile(r'(\d+)')
        return tuple(map(int, NEW_DATE_STR.findall(cls.date_str)))

    @staticmethod
    def valid_date_a(specie):
            date = specie.format_date()
            if 1 < date[0] < 31 and 1 < date[1] <= 12 and len(str(date[2])) == 4:
                print(f'дата {date} валидна')
            else:
                print('Дата невалидна')

    @staticmethod
    def valid_date_b(date_str):
        NEW_DATE_STR = re.compile(r'(\d+)')
        date_tuple = tuple(map(int, NEW_DATE_STR.findall(date_str)))
        if 1 < date_tuple[0] < 31 and 1 < date_tuple[1] <= 12 and len(str(date_tuple[2])) == 4:
            print(f'дата {date_str} валидна')
        else:
            print('Дата невалидна')


a = Date('22-11-2021')
print(a.format_date())
Date.valid_date_b('22-12-1022')
